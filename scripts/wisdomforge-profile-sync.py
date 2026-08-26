#!/usr/bin/env python3
"""Diagnostic tool: compare a child Hermes profile's installed skills and config
against the current WisdomForge kids repo templates.

READ-ONLY. This script does not write to any file. It reports what differs so
the parent can review and apply changes manually.

Usage:
  # Check one child profile
  python3 scripts/wisdomforge-profile-sync.py \
    --child-profile ~/.hermes/profiles/willow \
    --kids-repo ~/projects/wisdomforge-kids-Hermes-profiles

  # Check all child profiles in a family directory
  python3 scripts/wisdomforge-profile-sync.py \
    --family-dir ~/.hermes/profiles \
    --kids-repo ~/projects/wisdomforge-kids-Hermes-profiles

  # Filter by band (little, middle, high)
  python3 scripts/wisdomforge-profile-sync.py \
    --family-dir ~/.hermes/profiles \
    --kids-repo ~/projects/wisdomforge-kids-Hermes-profiles \
    --band little

The script reads the kids repo's scaffold_child_profile.py to discover the
band-to-skills mapping, then compares each child profile's installed skills
against those templates.

Exit codes:
  0 = check completed (may have findings)
  1 = error (bad args, missing paths)
  2 = drift detected (findings exist — parent should review)
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import re
import sys
from pathlib import Path


# Band IDs matching the kids repo and the academy's bands.ts
BAND_IDS = {"little", "young", "emerging"}
# Map kids repo band names to our band IDs
BAND_MAP = {"elementary": "little", "middle": "young", "high": "emerging"}
# Reverse map for looking up kids repo files
BAND_REVERSE = {"little": "elementary", "young": "middle", "emerging": "high"}


def detect_band(child_dir: Path) -> str | None:
    """Try to detect the child's band from SOUL.md or config-snippet.yaml."""
    # Check SOUL.md for band references
    soul = child_dir / "SOUL.md"
    if soul.is_file():
        text = soul.read_text(encoding="utf-8", errors="replace").lower()
        for band_id in BAND_IDS:
            # Look for band identifiers in SOUL text
            if f"band: {band_id}" in text or f"band:{band_id}" in text:
                return band_id
            # Check for age range references
            if band_id == "little" and ("5–10" in text or "5-10" in text or "little thinker" in text):
                return band_id
            if band_id == "young" and ("11–14" in text or "11-14" in text or "young mind" in text):
                return band_id
            if band_id == "emerging" and ("15–18" in text or "15-18" in text or "emerging adult" in text):
                return band_id

    # Check config-snippet.yaml
    config = child_dir / "config-snippet.yaml"
    if config.is_file():
        text = config.read_text(encoding="utf-8", errors="replace").lower()
        for kids_band, our_band in BAND_MAP.items():
            if kids_band in text:
                return our_band

    return None


def parse_scaffold_bands(kids_repo: Path) -> dict[str, list[str]]:
    """Parse scripts/scaffold_child_profile.py to extract the band-to-skills mapping.

    Returns a dict mapping our band IDs (little/young/emerging) to lists of skill names.
    """
    scaffold = kids_repo / "scripts" / "scaffold_child_profile.py"
    if not scaffold.is_file():
        print(f"WARNING: {scaffold} not found — cannot determine recommended skills per band", file=sys.stderr)
        return {}

    text = scaffold.read_text(encoding="utf-8", errors="replace")

    # Extract the BANDS dict by finding skill names in the structure
    # The scaffold script has entries like: "wisdomforge-ritual", "socratic-homework", etc.
    # We parse by finding each band section and extracting quoted skill names
    bands: dict[str, list[str]] = {}

    # Find band keys and their skill lists
    # Pattern: "elementary": { ... "skills": [ ... ] }
    for kids_band, our_band in BAND_MAP.items():
        # Find the section for this band
        pattern = rf'"{kids_band}"\s*:\s*\{{[^}}]*?"skills"\s*:\s*\[(.*?)\]'
        match = re.search(pattern, text, re.DOTALL)
        if match:
            skills_block = match.group(1)
            skill_names = re.findall(r'"([^"]+)"', skills_block)
            bands[our_band] = skill_names
        else:
            # Fallback: try matching by looking at the structure differently
            print(f"WARNING: could not parse skills for band '{kids_band}' from scaffold script", file=sys.stderr)

    return bands


def file_hash(path: Path) -> str:
    """Return SHA-256 hash of file contents, or empty string if unreadable."""
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except Exception:
        return ""


def compare_skills(
    child_dir: Path,
    kids_repo: Path,
    band: str,
    recommended_skills: list[str],
) -> list[dict]:
    """Compare a child profile's installed skills against the kids repo templates.

    Returns a list of finding dicts.
    """
    findings: list[dict] = []
    child_skills_dir = child_dir / "skills"
    kids_skills_dir = kids_repo / "skills"

    # Check for missing skills (recommended but not installed)
    for skill_name in recommended_skills:
        child_skill = child_skills_dir / skill_name / "SKILL.md"
        kids_skill = kids_skills_dir / skill_name / "SKILL.md"

        if not child_skill.is_file():
            findings.append({
                "type": "missing_skill",
                "skill": skill_name,
                "detail": f"Recommended for band '{band}' but not installed in child profile",
                "kids_repo_path": str(kids_skill),
            })

    # Check for updated skills (installed but differs from template)
    for skill_name in recommended_skills:
        child_skill = child_skills_dir / skill_name / "SKILL.md"
        kids_skill = kids_skills_dir / skill_name / "SKILL.md"

        if child_skill.is_file() and kids_skill.is_file():
            child_hash = file_hash(child_skill)
            kids_hash = file_hash(kids_skill)
            if child_hash != kids_hash:
                # Generate a unified diff
                child_lines = child_skill.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
                kids_lines = kids_skill.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
                diff = list(difflib.unified_diff(
                    kids_lines, child_lines,
                    fromfile=f"kids-repo/skills/{skill_name}/SKILL.md",
                    tofile=f"child/skills/{skill_name}/SKILL.md",
                    n=2,
                ))
                diff_text = "".join(diff[:40])  # first 40 lines to keep output manageable
                if len(diff) > 40:
                    diff_text += f"\n... ({len(diff) - 40} more diff lines)"
                findings.append({
                    "type": "updated_skill",
                    "skill": skill_name,
                    "detail": f"Installed skill differs from kids repo template",
                    "diff": diff_text,
                })

    # Check for extra skills (installed but not in band recommendation)
    if child_skills_dir.is_dir():
        installed_skills = [d.name for d in child_skills_dir.iterdir() if d.is_dir() and (d / "SKILL.md").is_file()]
        for skill_name in installed_skills:
            if skill_name not in recommended_skills:
                findings.append({
                    "type": "extra_skill",
                    "skill": skill_name,
                    "detail": f"Installed but not in band '{band}' recommendation (may be parent-approved)",
                })

    return findings


def compare_config(
    child_dir: Path,
    kids_repo: Path,
    band: str,
) -> list[dict]:
    """Compare the child's config snippet against the band defaults in the kids repo."""
    findings: list[dict] = []
    kids_band = BAND_REVERSE.get(band, band)

    child_config = child_dir / "config-snippet.yaml"
    kids_config = kids_repo / "configs" / f"{kids_band}.yaml.snippet"

    if not kids_config.is_file():
        # No config template to compare against
        return findings

    if not child_config.is_file():
        findings.append({
            "type": "missing_config",
            "detail": f"No config-snippet.yaml in child profile (kids repo has {kids_band}.yaml.snippet)",
        })
        return findings

    child_hash = file_hash(child_config)
    kids_hash = file_hash(kids_config)
    if child_hash != kids_hash:
        child_lines = child_config.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
        kids_lines = kids_config.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
        diff = list(difflib.unified_diff(
            kids_lines, child_lines,
            fromfile=f"kids-repo/configs/{kids_band}.yaml.snippet",
            tofile=f"child/config-snippet.yaml",
            n=2,
        ))
        diff_text = "".join(diff[:30])
        if len(diff) > 30:
            diff_text += f"\n... ({len(diff) - 30} more diff lines)"
        findings.append({
            "type": "config_drift",
            "detail": f"Child config differs from band '{band}' defaults in kids repo",
            "diff": diff_text,
        })

    return findings


def check_identity_files(child_dir: Path) -> list[dict]:
    """Verify that identity files (SOUL.md, USER.md, MEMORY.md) exist and are non-empty."""
    findings: list[dict] = []
    for identity_file in ["SOUL.md", "USER.md", "MEMORY.md"]:
        path = child_dir / identity_file
        if not path.is_file():
            findings.append({
                "type": "missing_identity_file",
                "file": identity_file,
                "detail": f"{identity_file} is missing — this is a required identity file",
            })
        elif path.stat().st_size == 0:
            findings.append({
                "type": "empty_identity_file",
                "file": identity_file,
                "detail": f"{identity_file} is empty — this should not happen",
            })
    return findings


def check_profile(
    child_dir: Path,
    kids_repo: Path,
    band: str | None = None,
) -> list[dict]:
    """Run all checks on a single child profile and return findings."""
    all_findings: list[dict] = []

    # Detect band if not provided
    if band is None:
        band = detect_band(child_dir)
        if band is None:
            all_findings.append({
                "type": "unknown_band",
                "detail": "Could not detect band from SOUL.md or config-snippet.yaml. Use --band to specify.",
            })
            # Still check identity files even without band
            all_findings.extend(check_identity_files(child_dir))
            return all_findings

    # Parse the kids repo for recommended skills
    band_skills = parse_scaffold_bands(kids_repo)
    recommended = band_skills.get(band, [])

    if not recommended:
        all_findings.append({
            "type": "no_skill_mapping",
            "detail": f"Could not determine recommended skills for band '{band}' from kids repo scaffold script.",
        })

    # Run checks
    all_findings.extend(check_identity_files(child_dir))
    all_findings.extend(compare_skills(child_dir, kids_repo, band, recommended))
    all_findings.extend(compare_config(child_dir, kids_repo, band))

    return all_findings


def is_child_profile(profile_dir: Path) -> bool:
    """Heuristic: does this directory look like a child profile?

    Checks for SOUL.md with WisdomForge references, or a design-record.md file.
    """
    soul = profile_dir / "SOUL.md"
    if soul.is_file():
        text = soul.read_text(encoding="utf-8", errors="replace").lower()
        if "wisdomforge" in text or "parent-operator" in text or "child" in text or "band" in text:
            return True

    # design-record.md is created by the scaffold script
    if (profile_dir / "design-record.md").is_file():
        return True

    return False


def print_findings(profile_name: str, band: str | None, findings: list[dict]) -> bool:
    """Print findings for a profile. Returns True if any drift was found."""
    has_drift = False

    print(f"\n{'='*60}")
    print(f"Profile: {profile_name}")
    print(f"Band: {band or 'unknown'}")
    print(f"{'='*60}")

    if not findings:
        print("  All checks passed. No drift detected.")
        print()
        return False

    for f in findings:
        ftype = f["type"]
        if ftype == "missing_skill":
            has_drift = True
            print(f"  [MISSING SKILL] {f['skill']}")
            print(f"    {f['detail']}")
            if "kids_repo_path" in f:
                print(f"    Template: {f['kids_repo_path']}")
        elif ftype == "updated_skill":
            has_drift = True
            print(f"  [UPDATED SKILL] {f['skill']}")
            print(f"    {f['detail']}")
            if "diff" in f:
                print(f"    --- diff (first lines) ---")
                for line in f["diff"].splitlines()[:15]:
                    print(f"    {line}")
                if len(f["diff"].splitlines()) > 15:
                    print(f"    ... (see full diff above)")
        elif ftype == "extra_skill":
            has_drift = True
            print(f"  [EXTRA SKILL] {f['skill']}")
            print(f"    {f['detail']}")
        elif ftype == "config_drift":
            has_drift = True
            print(f"  [CONFIG DRIFT]")
            print(f"    {f['detail']}")
            if "diff" in f:
                print(f"    --- diff (first lines) ---")
                for line in f["diff"].splitlines()[:10]:
                    print(f"    {line}")
        elif ftype == "missing_config":
            has_drift = True
            print(f"  [MISSING CONFIG]")
            print(f"    {f['detail']}")
        elif ftype == "missing_identity_file":
            has_drift = True
            print(f"  [MISSING IDENTITY FILE] {f['file']}")
            print(f"    {f['detail']}")
        elif ftype == "empty_identity_file":
            has_drift = True
            print(f"  [EMPTY IDENTITY FILE] {f['file']}")
            print(f"    {f['detail']}")
        elif ftype == "unknown_band":
            has_drift = True
            print(f"  [UNKNOWN BAND]")
            print(f"    {f['detail']}")
        elif ftype == "no_skill_mapping":
            has_drift = True
            print(f"  [NO SKILL MAPPING]")
            print(f"    {f['detail']}")
        else:
            print(f"  [UNKNOWN] {f}")
        print()

    return has_drift


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--child-profile",
        type=Path,
        help="Path to a single child profile directory (e.g. ~/.hermes/profiles/willow)",
    )
    group.add_argument(
        "--family-dir",
        type=Path,
        help="Path to a directory containing multiple child profiles (e.g. ~/.hermes/profiles)",
    )
    parser.add_argument(
        "--kids-repo",
        type=Path,
        required=True,
        help="Path to a local clone of smfworks/wisdomforge-kids-Hermes-profiles",
    )
    parser.add_argument(
        "--band",
        choices=sorted(BAND_IDS),
        help="Filter by band (only used with --family-dir). If omitted, bands are auto-detected.",
    )
    args = parser.parse_args()

    kids_repo = args.kids_repo.expanduser().resolve()
    if not kids_repo.is_dir():
        print(f"ERROR: kids-repo path does not exist: {kids_repo}", file=sys.stderr)
        return 1

    # Verify it looks like the kids repo
    if not (kids_repo / "BANDS.md").is_file() and not (kids_repo / "scripts" / "scaffold_child_profile.py").is_file():
        print(f"ERROR: {kids_repo} does not look like the wisdomforge-kids-Hermes-profiles repo", file=sys.stderr)
        print("       Expected: BANDS.md and scripts/scaffold_child_profile.py", file=sys.stderr)
        return 1

    any_drift = False

    if args.child_profile:
        child_dir = args.child_profile.expanduser().resolve()
        if not child_dir.is_dir():
            print(f"ERROR: child-profile path does not exist: {child_dir}", file=sys.stderr)
            return 1

        band = args.band
        if band is None:
            band = detect_band(child_dir)

        findings = check_profile(child_dir, kids_repo, band)
        if print_findings(child_dir.name, band, findings):
            any_drift = True
    else:
        family_dir = args.family_dir.expanduser().resolve()
        if not family_dir.is_dir():
            print(f"ERROR: family-dir path does not exist: {family_dir}", file=sys.stderr)
            return 1

        # Scan for child profiles
        child_profiles: list[tuple[str, Path, str | None]] = []
        for entry in sorted(family_dir.iterdir()):
            if entry.is_dir() and is_child_profile(entry):
                band = detect_band(entry)
                if args.band and band != args.band:
                    continue
                child_profiles.append((entry.name, entry, band))

        if not child_profiles:
            print(f"No child profiles found in {family_dir}", file=sys.stderr)
            if args.band:
                print(f"  (filtered by band: {args.band})", file=sys.stderr)
            print("  Tip: child profiles have SOUL.md with 'wisdomforge' or 'band' references, or a design-record.md", file=sys.stderr)
            return 0

        print(f"Found {len(child_profiles)} child profile(s) in {family_dir}")

        for name, path, band in child_profiles:
            findings = check_profile(path, kids_repo, band)
            if print_findings(name, band, findings):
                any_drift = True

    # Summary
    print(f"\n{'='*60}")
    if any_drift:
        print("SUMMARY: drift detected — review findings above and apply changes manually.")
        print("Remember: never overwrite SOUL.md, USER.md, or MEMORY.md during sync.")
        return 2
    else:
        print("SUMMARY: all profiles in sync. No drift detected.")
        return 0


if __name__ == "__main__":
    sys.exit(main())