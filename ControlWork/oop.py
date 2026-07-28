"""Задание 1"""
class Person:
    def __init__(self, age: int = 0):
        self.age = age 

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        self._age = value

"""Задание 2"""
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "I am an animal"

class Dog(Animal):
    def speak(self) -> str:
        return "Woof, woof"
    
class Cat(Animal):
    def speak(self) -> str:
        return "Meow, meow"

dog = Dog("Актош")
cat = Cat("Мурка")
print(dog.name, dog.speak()) 
print(cat.name, cat.speak())  


"""Задание 3"""
class Vehicle:
    def move(self) -> str:
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self) -> str:
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self) -> str:
        return "Bicycle is pedaling"

def move(vehicle: Vehicle) -> str:
    return vehicle.move()
car = Car()
bike = Bicycle()
print(move(car)) 
print(move(bike))


"""Задание 4"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())      
print(round(circle.area(), 2))