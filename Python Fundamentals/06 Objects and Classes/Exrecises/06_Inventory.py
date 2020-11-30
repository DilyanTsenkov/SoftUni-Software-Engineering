class Inventory:
    items = []

    def __init__(self, capacity):
        self.__capacity = capacity
        self.left_capacity = self.__capacity

    def add_item(self, item):
        if len(Inventory.items) < self.__capacity:
            Inventory.items.append(item)
            self.left_capacity -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        Inventory.items = ", ".join(Inventory.items)
        return f"Items: {Inventory.items}.\nCapacity left: {self.left_capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
inventory.add_item("bottle")

print(inventory.get_capacity())
print(inventory)
