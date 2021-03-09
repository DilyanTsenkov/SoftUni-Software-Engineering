class Lion:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    @staticmethod
    def get_needs():
        return 50


class Tiger:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    @staticmethod
    def get_needs():
        return 45


class Cheetah:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    @staticmethod
    def get_needs():
        return 60


class Keeper:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Caretaker:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Vet:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.name = name
        self.animals = []
        self.workers = []

    @staticmethod
    def separator(arg1, arg2):
        return [a for a in arg1 if type(a).__name__ == arg2]

    @staticmethod
    def printer(arg3):
        r = ""
        for a in arg3:
            r += a.__repr__() + "\n"
        return r.strip()

    def add_animal(self, animal, price):
        if self.__budget < price:
            return f"Not enough budget"
        if len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, worker_name):
        find_worker = [w for w in self.workers if w.name == worker_name]
        if not find_worker:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(find_worker[0])
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        needed_money = [w.salary for w in self.workers]
        if self.__budget < sum(needed_money):
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= sum(needed_money)
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needed_money = [a.get_needs() for a in self.animals]
        if self.__budget < sum(needed_money):
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= sum(needed_money)
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = self.separator(self.animals, "Lion")
        tigers = self.separator(self.animals, "Tiger")
        cheetahs = self.separator(self.animals, "Cheetah")
        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        result += f"{self.printer(lions)}\n"
        result += f"----- {len(tigers)} Tigers:\n"
        result += f"{self.printer(tigers)}\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += f"{self.printer(cheetahs)}"
        return result

    def workers_status(self):
        keepers = self.separator(self.workers, "Keeper")
        caretakers = self.separator(self.workers, "Caretaker")
        vets = self.separator(self.workers, "Vet")
        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        result += f"{self.printer(keepers)}\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += f"{self.printer(caretakers)}\n"
        result += f"----- {len(vets)} Vets:\n"
        result += f"{self.printer(vets)}"
        return result


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
           Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
           Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
           Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
