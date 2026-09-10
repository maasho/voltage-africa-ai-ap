"""Check repository skill discovery, role coverage, references and evaluation cases."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def validate(root):
    errors = []
    skill_root = root / ".agents" / "skills"
    skills = {}
    for path in sorted(skill_root.glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8-sig")
        frontmatter = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not frontmatter:
            errors.append(f"{path.relative_to(root)}: missing frontmatter")
            continue
        fields = dict(re.findall(r"^([a-z-]+): (.+)$", frontmatter[1], re.M))
        name = fields.get("name", "")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            errors.append(f"{path}: invalid name")
        if name != path.parent.name or name in skills:
            errors.append(f"{path}: duplicate or mismatched skill name")
        if not fields.get("description", "").strip():
            errors.append(f"{path}: missing description")
        skills[name] = path
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if "://" not in target and not target.startswith("#"):
                resolved = (path.parent / target.split("#")[0]).resolve()
                if not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
                    errors.append(f"{path}: broken or out-of-repo reference {target}")
    registry = json.loads((root / "marketing-team/skill-map.json").read_text(encoding="utf-8"))
    mapped = []
    primaries = []
    for entry in registry["roles"]:
        role = entry["role"]
        mapped.append(role)
        primaries.append(entry["primary_skill"])
        role_path = root / role
        if not role_path.is_file():
            errors.append(f"Missing role: {role}")
        elif entry["primary_skill"] not in role_path.read_text(encoding="utf-8"):
            errors.append(f"Role does not reference its primary skill: {role}")
        for name in [entry["primary_skill"], *entry["supporting_skills"]]:
            if name not in skills:
                errors.append(f"Unknown skill {name} for {role}")
    actual = {p.relative_to(root).as_posix() for p in (root / "marketing-team/agents").glob("*.md")}
    if len(mapped) != len(set(mapped)) or set(mapped) != actual:
        errors.append("Role registry has duplicate or missing roles")
    if len(primaries) != len(set(primaries)):
        errors.append("Primary skill is assigned to multiple roles")
    cases = json.loads((root / "docs/skill-eval-cases.json").read_text(encoding="utf-8"))
    if {c["skill"] for c in cases} != set(primaries):
        errors.append("Evaluation cases do not cover every primary skill")
    for case in cases:
        if not case.get("prompt") or not case.get("expected_behavior"):
            errors.append("Evaluation case missing prompt or expected behavior")
    return errors, len(skills), len(mapped)

if __name__ == "__main__":
    issues, skills, roles = validate(ROOT)
    for issue in issues:
        print(issue)
    print(f"{skills} skills, {roles} roles, {len(issues)} structural errors")
    raise SystemExit(bool(issues))
