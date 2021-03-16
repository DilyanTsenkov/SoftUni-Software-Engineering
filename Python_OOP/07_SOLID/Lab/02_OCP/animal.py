from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def get_sound(self):
        pass


class Cat(Animal):
    sound = 'meow'

    def get_sound(self):
        return self.sound


class Dog(Animal):
    sound = 'woof-woof'

    def get_sound(self):
        return self.sound


class Chicken(Animal):
    sound = 'piu-piu'

    def get_sound(self):
        return self.sound


def animal_sound(animal_species: list):
    for animal in animal_species:
        print(animal.get_sound())


animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)
