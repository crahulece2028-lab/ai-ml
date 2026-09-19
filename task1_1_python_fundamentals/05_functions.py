"""Week 1 - Exercise 5: Functions.

Covers: args/kwargs, *args/**kwargs, lambdas, default args, closures, recursion.
Run:  python 05_functions.py
"""


def area_rectangle(length=1, width=1):
    return length * width


def apply(*args, func=lambda x: x):
    return [func(a) for a in args]


def build_power(exponent):
    def power(base):
        return base ** exponent
    return power


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def summarize_scores(name, *scores, **options):
    avg = sum(scores) / len(scores)
    rounding = options.get("round", 2)
    return f"{name}: avg {round(avg, rounding)} across {len(scores)} scores"


def compose(f, g):
    return lambda x: f(g(x))


if __name__ == "__main__":
    print("area_rectangle()", area_rectangle())
    print("area_rectangle(4, 2)", area_rectangle(4, 2))
    print("square:", apply(1, 2, 3, func=lambda x: x * x))
    square = build_power(2)
    print("closures 3^2:", square(3), "3^3:", build_power(3)(3))
    print("factorial(6):", factorial(6))
    print("gcd(48, 36):", gcd(48, 36))
    print(summarize_scores("Rahul", 78, 85, 92, round=1))
    add_double = compose(lambda x: x + 1, lambda x: x * 2)
    print("compose add1(2x)(5):", add_double(5))
    assert area_rectangle() == 1 and area_rectangle(4, 2) == 8
    assert apply(1, 2, 3, func=lambda x: x * x) == [1, 4, 9]
    assert square(3) == 9 and build_power(3)(3) == 27
    assert factorial(6) == 720 and gcd(48, 36) == 12
    print("\nAll exercises passed.")