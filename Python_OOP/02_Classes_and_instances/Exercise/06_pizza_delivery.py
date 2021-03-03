class PizzaDelivery:

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = float(price)
        self.ingredients = dict(ingredients)
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        elif ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity
        ingredients_price = quantity * ingredient_price
        self.price += ingredients_price

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {str(self.name)}!"
        elif self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"
        self.ingredients[ingredient] -= quantity
        ingredients_price = quantity * ingredient_price
        self.price -= ingredients_price

    def make_order(self):
        self.ordered = True
        pizza_ingredients = [f"{i}: {q}" for i, q in self.ingredients.items()]
        if self.price % 1 == 0:
            self.price = int(self.price)
        return f"You've ordered pizza {self.name} prepared with {', '.join(pizza_ingredients)} and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 1)
margarita.add_extra('cheese', 1, 0.5)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
