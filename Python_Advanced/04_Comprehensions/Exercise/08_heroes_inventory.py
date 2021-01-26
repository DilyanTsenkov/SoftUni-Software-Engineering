def the_end(given_items):
    if given_items == "End":
        return True


heroes = {hero: [] for hero in input().split(", ")}

while True:
    given_items = input()
    if the_end(given_items):
        break
    name, item, cost = given_items.split("-")
    found = [True for el in heroes[name] if el[0] == item]
    if not found:
        heroes[name].append([item, cost])

for key, value in heroes.items():
    costs = [int(el[1]) for el in value]
    print(f"{key} -> Items: {len(value)}, Cost: {sum(costs)}")
