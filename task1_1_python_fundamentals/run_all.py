"""Runs every exercise file in this folder sequentially.

Run:  python run_all.py
"""

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
FILES = [
    "01_variables_basics.py",
    "02_lists_and_tuples.py",
    "03_dictionaries_and_sets.py",
    "04_conditionals_and_loops.py",
    "05_functions.py",
    "06_file_handling.py",
    "07_exceptions.py",
    "08_oop.py",
]

failed = []
for name in FILES:
    result = subprocess.run(
        [sys.executable, str(HERE / name)],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    status = "PASS" if result.returncode == 0 else "FAIL"
    print(f"[{status}] {name}")
    if result.returncode != 0:
        failed.append(name)
        print(result.stderr)

if failed:
    print(f"\n{len(failed)} file(s) failed: {failed}")
    sys.exit(1)

print("\nAll exercise modules passed.")