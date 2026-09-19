"""Week 1 - Exercise 6: File Handling.

Covers: reading/writing text, CSV parsing, JSON load/dump, context managers.
Uses temp files so nothing needs to exist beforehand.
Run:  python 06_file_handling.py
"""

import csv
import json
import os
import tempfile


def write_and_read(tmp, text):
    path = os.path.join(tmp, "notes.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def count_words_in_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return len(f.read().split())


def write_and_read_csv(tmp, rows):
    path = os.path.join(tmp, "data.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["city", "pop_millions"])
        writer.writerows(rows)
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def csv_sum_column(path, column):
    total = 0
    with open(path, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            total += float(row[column])
    return total


def write_and_read_json(tmp, obj):
    path = os.path.join(tmp, "model.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def append_lines(tmp, lines):
    path = os.path.join(tmp, "log.txt")
    mode = "a" if True else "w"
    with open(path, mode, encoding="utf-8") as f:
        f.writelines(line + "\n" for line in lines)
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip().splitlines()


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        text = "machine learning is fun\npython is powerful"
        print("write+read:", repr(write_and_read(tmp, text)))

        p = os.path.join(tmp, "notes.txt")
        with open(p, "w", encoding="utf-8") as f:
            f.write("one two three")
        print("word count:", count_words_in_file(p))

        rows = [("Mumbai", 20.7), ("Delhi", 16.3), ("Kolkata", 14.8)]
        csv_data = write_and_read_csv(tmp, rows)
        print("csv rows:", csv_data)
        p = os.path.join(tmp, "data.csv")
        print("csv sum(pop_millions):", csv_sum_column(p, "pop_millions"))

        result = write_and_read_json(tmp, {"model": "linear", "params": {"lr": 0.01}})
        print("json roundtrip:", result)

        print("append:", append_lines(tmp, ["2026-01-01 OK", "2026-01-02 OK"]))

    print("\nAll exercises passed.")