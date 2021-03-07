class Customer:
    c_id = 0

    def __init__(self, name, address, email):
        Customer.c_id += 1
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.c_id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer.c_id + 1

class Equipment:
    e_id = 0

    def __init__(self, name):
        Equipment.e_id += 1
        self.name = name
        self.id = Equipment.e_id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.e_id + 1

class ExercisePlan:
    p_id = 0

    def __init__(self, trainer_id, equipment_id, duration):
        ExercisePlan.p_id += 1
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.p_id

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        minutes = hours * 60
        return cls(trainer_id, equipment_id, minutes)

    @staticmethod
    def get_next_id():
        return ExercisePlan.p_id + 1

class Trainer:
    t_id = 0

    def __init__(self, name):
        Trainer.t_id += 1
        self.name = name
        self.id = Trainer.t_id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.t_id + 1

class Subscription:
    s_id = 0

    def __init__(self, date, customer_id, trainer_id, exercise_id):
        Subscription.s_id += 1
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = Subscription.s_id
        Subscription.s_id += 1

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"

    @staticmethod
    def get_next_id():
        return Subscription.s_id + 1

class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        current_sub = [sub for sub in self.subscriptions if sub.id == subscription_id]
        current_customer = [c for c in self.customers if c.id == current_sub[0].customer_id]
        current_trainer = [t for t in self.trainers if t.id == current_sub[0].trainer_id]
        current_plan = [p for p in self.plans if p.trainer_id == current_sub[0].trainer_id]
        current_equipment = [e for e in self.equipment if e.id == current_plan[0].equipment_id]
        return f"{current_sub[0]}\n{current_customer[0]}\n{current_trainer[0]}\n{current_equipment[0]}\n{current_plan[0]}"




customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))