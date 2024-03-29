class Room:
    appliance_types = ()
    room_cost = 0

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0
        self.appliances = self.generate_appliances(*self.appliance_types)

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        self.__validate_expenses(value)
        self.__expenses = value

    @property
    def total_expenses(self):
        return self.expenses + self.room_cost

    def calculate_expenses(self, *args):
        result = 0
        for items in args:
            result += sum(
                a.get_monthly_expense() for a in items
            )
        self.expenses = result

    def generate_appliances(self, *appliance_types):
        appliances = []
        for _ in range(self.members_count):
            for appliance_type in appliance_types:
                appliances.append(appliance_type())
        return appliances

    def get_consumers_total_cost(self):
        children_results = [
            f'--- Child {i + 1} monthly cost: {child.get_monthly_expense():.2f}$'
            for (i, child) in enumerate(self.children)
        ]
        return [
            *children_results,
            f'--- Appliances monthly cost: {sum(a.get_monthly_expense() for a in self.appliances):.2f}$',
        ]

    @staticmethod
    def __validate_expenses(value):
        if value < 0:
            raise ValueError('Expenses cannot be negative')

    def __repr__(self):
        consumers_results = self.get_consumers_total_cost()
        result = [
            f'{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$',
            *consumers_results,
        ]

        return '\n'.join(result)

