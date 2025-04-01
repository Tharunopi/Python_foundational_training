from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def status(self):
        print("sleeping")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()
d.status()