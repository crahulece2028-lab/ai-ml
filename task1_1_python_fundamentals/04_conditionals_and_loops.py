"""Week 1 - Exercise 4: Conditionals & Loops.

Covers: for/while loops, fizzbuzz, prime detection, pattern printing, range.
Run:  python 04_conditionals_and_loops.py
"""


def fizzbuzz(n):
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return out


def sum_even_up_to(n):
    total = 0
    i = 1
    while i <= n:
        if i % 2 == 0:
            total += i
        i += 1
    return total


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def prime_list_up_to(n):
    return [x for x in range(2, n + 1) if is_prime(x)]


def print_triangle(n):
    return ["".join(str(x) for x in range(1, i + 1)) for i in range(1, n + 1)]


def classify_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


if __name__ == "__main__":
    print("FizzBuzz 1..15:", fizzbuzz(15))
    print("Sum of evens <= 100:", sum_even_up_to(100))
    print("Primes up to 50:", prime_list_up_to(50))
    print("Triangle:", print_triangle(5))
    print("Grade 74 ->", classify_grade(74))
    assert fizzbuzz(15)[-1] == "FizzBuzz"
    assert is_prime(2) and is_prime(97) and not is_prime(1)
    assert classify_grade(74) == "C"
    print("\nAll exercises passed.")