#!/usr/bin/env python3
import argparse
import sys

TEMPLATES = {
    "planning": """You are designing in Pencil/OpenPencil via MCP.\n\nTask:\nCreate a design execution plan for this request: {task}\n\nHard rules:\n- Do not create or modify nodes yet.\n- Only produce a structured plan.\n- Break the work into pages, sections, and components.\n- Identify reusable tokens, layout rules, and visual constraints.\n- Flag any ambiguity before execution.\n\nReturn:\n1. pages\n2. sections per page\n3. component inventory\n4. token/style plan\n5. execution order\n6. risk points\n7. verification checkpoints\n""",
    "skeleton": """Build only the structural skeleton for the approved plan.\n\nTask:\n{task}\n\nHard rules:\n- Create only pages, frames, sections, groups, and layout containers.\n- Do not polish visuals.\n- Do not generate final copy unless placeholder text is required.\n- Use clear hierarchy and autolayout where appropriate.\n- Keep naming explicit and reusable.\n\nAfter execution, report:\n1. created pages\n2. created sections/frames\n3. layout structure used\n4. unresolved structure risks\n""",
    "section": """Fill content for only this section: {section}\n\nTask:\n{task}\n\nHard rules:\n- Modify only the target section.\n- Do not touch other pages or sections.\n- Re-read the relevant nodes before editing.\n- Keep structure stable unless a local fix is necessary.\n- If a conflict appears, stop and report it.\n\nReturn:\n1. nodes changed\n2. nodes created\n3. text/content inserted\n4. tokens/styles applied\n5. anything needing confirmation\n""",
    "refine": """Refine the current design for consistency and polish.\n\nTask:\n{task}\n\nHard rules:\n- Do not restructure the information architecture.\n- Do not add new sections unless strictly necessary.\n- Focus only on spacing, alignment, typography consistency, color/token consistency, and emphasis hierarchy.\n- Keep the existing component logic intact.\n\nReturn:\n1. refinements made\n2. consistency fixes\n3. remaining weak spots\n""",
    "safety": """Before making further changes, validate the current page tree and target nodes.\n\nTask:\n{task}\n\nIf any of the following happens, stop and report instead of continuing:\n- stale page tree\n- missing target node\n- cross-section mutation conflict\n- transport/MCP instability\n- permission mismatch\n\nIf MCP is unavailable, switch to fallback guidance mode instead of guessing.\n""",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a phase-specific OpenPencil prompt scaffold.")
    parser.add_argument("phase", choices=sorted(TEMPLATES.keys()))
    parser.add_argument("task", help="Task description")
    parser.add_argument("--section", default="TARGET_SECTION", help="Section name for section phase")
    args = parser.parse_args()

    template = TEMPLATES[args.phase]
    sys.stdout.write(template.format(task=args.task, section=args.section))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
