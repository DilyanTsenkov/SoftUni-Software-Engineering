class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, x):
        temp_name = self.name
        temp_surname = x.surname
        return Person(temp_name,temp_surname)

    def __str__(self):
        return str(self.name) + " " + str(self.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = list(people)

    def __repr__(self):
        self.members = [p.name + " " + p.surname for p in self.people]
        return f"Group {self.name} with members {', '.join(self.members)}"

    def __len__(self):
        return len(self.people)

    def __add__(self, x):
        temp_name = self.name + x.name
        temp_people = self.people + x.people
        return Group(temp_name, temp_people)

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index].name + ' ' + self.people[index].surname}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)

