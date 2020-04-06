class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute


c = Clock(12, 24)
print(c.hour)
c.hour = 13
c.hour
del c.hour


class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price


interestng_book = Book("Atomic Habits", 16.20)

# Access instance and class attributes
interestng_book.__dict__

vars(interestng_book)

vars(Book)


from abc import ABC, abstractmethod


class Validator(ABC):
    def __init__(self, initial):
        self.initial = initial

    def __set_name__(self, instance, name):
        self.name = name

    def __get__(self, instance, obj_type):
        return vars(instance).get(self.name, self.initial)

    def __set__(self, instance, value):
        self.validate(value)
        vars(instance)[self.name] = value

    @abstractmethod
    def validate(self, value):
        """Validate the given value."""


class NonNegative(Validator):
    def validate(self, value):
        if value < 1:
            raise ValueError("Positive number required")


class cached_property:
    def __init__(self, func):
        self.func = func

    def __set_name__(self, obj_type, name):
        self.name = name

    def __get__(self, instance, obj_type):
        print("Computing...")
        value = self.func(instance)
        vars(instance)[self.name] = value
        return value


from datetime import datetime


class Person:
    def __init__(self, name, born):
        self.name = name
        self.born = born

    @cached_property
    def age(self):
        current_year = datetime.now().year
        return current_year - self.born


j = Person("Jamie", 1980)
j.age
j.age
del j.age
j.age
j.age
