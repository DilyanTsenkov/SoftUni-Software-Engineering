class Customer:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self):
        rented_dvds = len(self.rented_dvds)
        rented_movies = [dvd.name for dvd in self.rented_dvds]
        return f"{self.id}: {self.name} of age {self.age} has {rented_dvds} rented DVD's ({', '.join(rented_movies)})"


class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {self.status()}"

    @classmethod
    def from_date(cls, current_id, name, date, age_restriction):
        month = cls.num_to_month()[int(date[3:5])]
        return cls(name, current_id, int(date[6::]), month, age_restriction)

    @staticmethod
    def num_to_month():
        return {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'August',
                9: 'September', 10: 'October',
                11: 'November', 12: 'December'}

    def status(self):
        if self.is_rented:
            return "rented"
        return "not rented"


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += customer.__repr__() + "\n"
        for dvd in self.dvds:
            result += dvd.__repr__() + "\n"
        return result.strip()

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        current_customer = [customer for customer in self.customers if customer_id == customer.id]
        movie = [dvd for dvd in self.dvds if dvd_id == dvd.id]
        if movie[0] in current_customer[0].rented_dvds:
            return f"{current_customer[0].name} has already rented {movie[0].name}"
        if movie[0].is_rented:
            return "DVD is already rented"
        if movie[0].age_restriction > current_customer[0].age:
            return f"{current_customer[0].name} should be at least {movie[0].age_restriction} to rent this movie"
        current_customer[0].rented_dvds.append(movie[0])
        movie[0].is_rented = True
        return f"{current_customer[0].name} has successfully rented {movie[0].name}"

    def return_dvd(self, customer_id, dvd_id):
        current_customer = [customer for customer in self.customers if customer_id == customer.id]
        movie = [dvd for dvd in current_customer[0].rented_dvds if dvd_id == dvd.id]
        if movie:
            current_customer[0].rented_dvds.remove(movie[0])
            customer_name = current_customer[0].name
            dvd_name = movie[0].name
            movie[0].is_rented = False
            return f"{customer_name} has successfully returned {dvd_name}"
        return f"{current_customer[0].name} does not have that DVD"


from project.customer import Customer
from project.dvd import DVD
from project.movie_world import MovieWorld

c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world)
