class Appliance:
    days_in_month = 30

    def __init__(self, cost: float):
        self.cost = cost

    def get_monthly_expense(self):
        one_month_costs = self.cost * self.days_in_month
        return one_month_costs
