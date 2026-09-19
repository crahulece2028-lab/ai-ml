"""Week 1 - Exercise 2: Lists & Tuples.

Covers: list ops, slicing, comprehensions, tuple unpacking, in-place vs copy.
Run:  python 02_lists_and_tuples.py
"""


def ex1_reverse_copy():
    nums = [1, 2, 3, 4, 5]
    return nums[::-1]


def ex2_evens_squares():
    return [n * n for n in range(1, 21) if n % 2 == 0]


def ex3_list_stats():
    data = [4.0, 3.5, 5.0, 4.2, 3.9]
    return sum(data) / len(data), max(data), min(data)


def ex4_second_largest():
    data = [10, 4, 8, 3, 9, 7]
    unique = sorted(set(data))
    assert len(unique) >= 2
    return unique[-2]


def ex5_tuple_unpack():
    student = ("Riya", "AI/ML", 3.9)
    name, dept, cgpa = student
    return name, dept, cgpa


def ex6_remove_duplicates_preserve_order():
    items = ["a", "b", "a", "c", "b", "d"]
    return list(dict.fromkeys(items))


def ex7_matrix_transpose():
    m = [[1, 2, 3], [4, 5, 6]]
    return [list(row) for row in zip(*m)]


if __name__ == "__main__":
    print("Reversed:", ex1_reverse_copy())
    print("Even squares (1-20):", ex2_evens_squares())
    print("Mean/max/min:", ex3_list_stats())
    print("Second largest:", ex4_second_largest())
    print("Unpacked:", ex5_tuple_unpack())
    print("Deduped:", ex6_remove_duplicates_preserve_order())
    print("Transpose:", ex7_matrix_transpose())
    assert ex7_matrix_transpose() == [[1, 4], [2, 5], [3, 6]]
    print("\nAll exercises passed.")