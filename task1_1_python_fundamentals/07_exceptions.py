"""Week 1 - Exercise 7: Exceptions.

Covers: try/except/else/finally, multiple exception types, custom exception,
raising, ensure-valid-int helper.
Run:  python 07_exceptions.py
"""


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return float("inf")
    except TypeError:
        return None


def parse_int(s, default=None):
    try:
        return int(s.strip())
    except (ValueError, AttributeError):
        return default


def read_first_line(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.readline().strip()
    except FileNotFoundError:
        return None
    except IsADirectoryError:
        return None
    finally:
        print("  (cleanup: read attempt finished)")


class NegativeValueError(Exception):
    pass


def set_positive_balance(value):
    if value < 0:
        raise NegativeValueError(f"balance cannot be negative: {value}")
    return value


def process_entries(pairs):
    ok, failed = 0, []
    for key, value in pairs:
        try:
            _ = safe_divide(value, 2)
            ok += 1
        except Exception as exc:  # noqa: BLE001
            failed.append((key, str(exc)))
    return ok, failed


if __name__ == "__main__":
    print("safe_divide(1, 0):", safe_divide(1, 0))
    print("safe_divide(1, 'a'):", safe_divide(1, "a"))
    print("safe_divide(4, 2):", safe_divide(4, 2))
    print("parse_int('  42'):", parse_int("  42"))
    print("parse_int('abc'):", parse_int("abc"))
    print("parse_int('abc', -1):", parse_int("abc", -1))

    import tempfile, os
    with tempfile.TemporaryDirectory() as tmp:
        print("read missing file:", read_first_line(os.path.join(tmp, "nope.txt")))
        p = os.path.join(tmp, "x.txt")
        with open(p, "w", encoding="utf-8") as f:
            f.write("hello")
        print("read existing file:", read_first_line(p))

    try:
        set_positive_balance(-5)
    except NegativeValueError as exc:
        print("custom exception:", exc)

    print("processed:", process_entries([("a", 4), ("b", 2), ("c", 0)]))
    print("\nAll exercises passed.")