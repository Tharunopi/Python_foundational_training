class Animal:
    def sound(self):
        print("Animal sounds")
    
class Dog(Animal):
    def sound(self):
        print("Dog barks")
    
class Cat(Animal):
    def sound(self):
        print("Cat Meow")

d = Dog()
c = Cat()
d.sound()
c.sound()