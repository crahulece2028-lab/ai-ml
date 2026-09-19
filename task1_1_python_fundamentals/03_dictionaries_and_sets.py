"""Week 1 - Exercise 3: Dictionaries & Sets.

Covers: dict CRUD, nested dicts, defaultdict-style counting, set operations.
Run:  python 03_dictionaries_and_sets.py
"""


def ex1_word_frequency(text):
    words = text.lower().replace(".", "").split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def ex2_merge_scores():
    a = {"ram": 42, "shyam": 51, "gita": 47}
    b = {"gita": 47, "sita": 38, "ram": 42}
    merged = {}
    for d in (a, b):
        for k, v in d.items():
            merged.setdefault(k, []).append(v)
    return merged


def ex3_top_scorer(d):
    return max(d, key=d.get)


def ex4_set_ops():
    ml = {"numpy", "pandas", "sklearn", "torch"}
    web = {"django", "flask", "fastapi"}
    core = {"numpy", "pandas", "torch", "django"}
    return {
        "students": len(ml | web | core),
        "ml_and_core": ml & core,
        "ml_only": ml - core - web,
        "symmetric_diff": ml ^ web,
    }


def ex5_flip_dict():
    d = {"a": 1, "b": 2, "c": 3}
    return {v: k for k, v in d.items()}


def ex6_count_chars(s):
    counts = {}
    for ch in s:
        if ch != " ":
            counts[ch] = counts.get(ch, 0) + 1
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)


if __name__ == "__main__":
    freq = ex1_word_frequency("ML ML AI data AI ML")
    print("Word frequency:", freq)
    assert freq.get("ml") == 3
    print("Merged scores:", ex2_merge_scores())
    print("Top scorer:", ex3_top_scorer(freq))
    print("Set ops:", ex4_set_ops())
    print("Flipped dict:", ex5_flip_dict())
    print("Char counts:", ex6_count_chars("data science rocks"))
    print("\nAll exercises passed.")