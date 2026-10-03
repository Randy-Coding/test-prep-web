"""Validate every C snippet that the CSE 320 UI renders as a code block."""

import importlib.util
import json
import re
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks" / "CSE320.py"
APP = ROOT / "app.js"


def load_questions():
    spec = importlib.util.spec_from_file_location("cse320_bank", BANK)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.questions


def displayed_code_blocks():
    snippets = []
    seen = set()
    pattern = re.compile(r"```[\w+-]*\n?([\s\S]*?)```|`([^`]+)`")
    for entries in load_questions().values():
        for question, record in entries.items():
            texts = [question]
            if isinstance(record, dict):
                texts.extend(
                    [record.get("answer", ""), record.get("explanation", "")]
                )
                texts.extend((record.get("choices") or {}).values())
            for text in texts:
                for fenced, inline in pattern.findall(str(text)):
                    code = fenced or inline
                    is_block = bool(fenced) or "\n" in code or ";" in code or "{" in code or len(code) > 60
                    if is_block and code not in seen:
                        seen.add(code)
                        snippets.append(code)
    return snippets


def format_as_ui(snippets):
    script = r"""
const fs = require('fs');
const source = fs.readFileSync(process.argv[1], 'utf8');
const start = source.indexOf('function formatCodeBlock');
const end = source.indexOf('\nfunction renderFormatted', start);
if (start < 0 || end < 0) throw new Error('formatCodeBlock was not found');
eval(source.slice(start, end));
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
process.stdout.write(JSON.stringify(input.map(formatCodeBlock)));
"""
    result = subprocess.run(
        ["node", "-e", script, str(APP)],
        input=json.dumps(snippets),
        text=True,
        capture_output=True,
        check=True,
    )
    return json.loads(result.stdout)


def translation_unit(code):
    function_definition = re.search(
        r"\b(?:int|void|long|double|float|char)\s+\w+\s*\([^;]*\)\s*\{",
        code,
    )
    if function_definition:
        return "#include <stddef.h>\n" + code + "\n"
    array_declaration = "int a[4][8] = {{0}};" if "a[i][j]" in code else "int a[64] = {0};"
    prelude = f"""
#include <stddef.h>
int n = 8, i = 0, j = 0, pass = 0, x = 0, y = 0, v = 0, sum = 0;
{array_declaration}
int b[64] = {{0}};
int *p = &x, *q = &y;
void use(int value);
int square(int value);
void unknown(void);
void validate_snippet(void) {{
"""
    return prelude + code + "\n}\n"


def main():
    raw = displayed_code_blocks()
    formatted = format_as_ui(raw)
    failures = []
    with tempfile.TemporaryDirectory(prefix="cse320-code-") as directory:
        directory = Path(directory)
        for index, (source, code) in enumerate(zip(raw, formatted), start=1):
            unbraced_loop = next(
                (
                    line
                    for line in code.splitlines()
                    if line.lstrip().startswith("for ") and not line.rstrip().endswith("{")
                ),
                None,
            )
            if unbraced_loop:
                failures.append(
                    (source, code, f"Displayed loop lacks explicit braces: {unbraced_loop}")
                )
                continue
            path = directory / f"snippet_{index}.c"
            path.write_text(translation_unit(code), encoding="utf-8")
            result = subprocess.run(
                ["clang", "-std=c11", "-fsyntax-only", "-Werror", str(path)],
                text=True,
                capture_output=True,
            )
            if result.returncode:
                failures.append((source, code, result.stderr.strip()))
    if failures:
        for source, code, error in failures:
            print("SOURCE:\n" + source)
            print("RENDERED:\n" + code)
            print(error + "\n")
        raise SystemExit(f"{len(failures)} C snippet(s) failed validation")
    print(f"Validated {len(formatted)} rendered C code blocks with Clang.")


if __name__ == "__main__":
    main()
