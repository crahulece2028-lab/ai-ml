"""Week 1 - Exercise 8: Object Oriented Programming.

Covers: classes, inheritance, methods, properties, dunder methods, polymorphism,
abstract-like base via plain classes, classmethods.
Run:  python 08_oop.py
"""


class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    @property
    def balance(self):
        return self._balance

    def __repr__(self):
        return f"BankAccount({self.owner!r}, {self._balance!r})"


class SavingsAccount(BankAccount):
    INTEREST_RATE = 0.04

    def apply_interest(self):
        self._balance += self._balance * self.INTEREST_RATE

    @classmethod
    def from_string(cls, data):
        owner, balance = data.split(",")
        return cls(owner.strip(), float(balance))


class Shape:
    def name(self):
        return type(self).__name__

    def area(self):
        raise NotImplementedError

    def __str__(self):
        return f"{self.name()} with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.141592653589793 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades or []

    def add_grade(self, grade):
        self.grades.append(grade)

    @property
    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

    def __eq__(self, other):
        return isinstance(other, Student) and other.name == self.name

    def __lt__(self, other):
        return self.average < other.average

    def __repr__(self):
        return f"Student({self.name!r}, avg={self.average:.2f})"


if __name__ == "__main__":
    acc = BankAccount("Rahul", 100)
    acc.deposit(50)
    acc.withdraw(30)
    print("balance:", acc.balance, "|", repr(acc))

    savings = SavingsAccount.from_string("Meera, 500")
    savings.deposit(100)
    savings.apply_interest()
    print("savings after interest:", savings.balance)

    shapes = [Circle(2), Rectangle(3, 4)]
    for shape in shapes:
        print(str(shape))
    assert Circle(2).area() > 12 and Rectangle(3, 4).area() == 12

    s1 = Student("Ali", [70, 80])
    s2 = Student("Bob", [90])
    print(s1 == Student("Ali", [65, 65]))   # same name -> equal
    print(s2 > s1)
    print(sorted([s1, s2]))
    assert (s1 == Student("Ali")) is True
    assert s2 > s1
    print("\nAll exercises passed.")