"""Week 1 - Exercise 1: Variables & Basic Types.

Covers: variable assignment, numeric types, strings, f-strings, type().
Run:  python 01_variables_basics.py
"""


def exercise_1_swap():
    a, b = 5, 10
    a, b = b, a
    assert a == 10 and b == 5
    return a, b


def exercise_2_calculate():
    base = 12
    height = 7
    area = 0.5 * base * height
    assert area == 42.0
    return area


def exercise_3_f_string():
    name = "Aarav"
    age = 24
    city = "Bengaluru"
    s = f"{name} is {age} years old and lives in {city}."
    assert s == "Aarav is 24 years old and lives in Bengaluru."
    return s


def exercise_4_types():
    values = [42, 3.14, "ML", True, None]
    type_names = {v: type(v).__name__ for v in values}
    assert type_names[42] == "int"
    assert type_names[3.14] == "float"
    assert type_names["ML"] == "str"
    assert type_names[True] == "bool"
    assert type_names[None] == "NoneType"
    return type_names


def exercise_5_even_odd():
    n = 17
    parity = "odd" if n % 2 else "even"
    assert parity == "odd"
    return parity


if __name__ == "__main__":
    print("Swap result:", exercise_1_swap())
    print("Triangle area:", exercise_2_calculate())
    print("Intro sentence:", exercise_3_f_string())
    print("Types:", exercise_4_types())
    print("Parity of 17:", exercise_5_even_odd())
    print("\nAll exercises passed.")