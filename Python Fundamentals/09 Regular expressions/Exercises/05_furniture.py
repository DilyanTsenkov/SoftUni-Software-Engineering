import re

money_spend = 0
furniture_list = []

while True:
    input_data = input()
    if input_data == "Purchase":
        break

    regex = r"^>{2}(?P<furniture>[A-Z][A-Za-z]+)<{2}(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)$"
    items = re.finditer(regex, input_data)

    for item in items:
        d = item.groupdict()
        furniture = d["furniture"]
        price = float(d["price"])
        quantity = int(d["quantity"])
        furniture_list.append(furniture)
        money_spend += (price * quantity)

print("Bought furniture:")
if len(furniture_list) > 0:
    print("\n".join(furniture_list))
print(f"Total money spend: {money_spend:.2f}")