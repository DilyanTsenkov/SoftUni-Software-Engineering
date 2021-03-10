class Animal:
    def eat(self):
        return "eating..."


class Dog(Animal):
    def bark(self):
        return "barking..."


animal = Animal()
print(animal.eat())
dog = Dog()
print(dog.eat())
