class Animal:
    def eat(self):
        return "eating..."


class Dog(Animal):
    def bark(self):
        return "barking..."


class Cat(Animal):
    def meow(self):
        return "meowing..."


animal = Animal()
dog = Dog()
cat = Cat()

print(dog.eat())
print(cat.eat())
print(cat.meow())
print(animal.eat())
