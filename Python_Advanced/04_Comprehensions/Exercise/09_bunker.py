categories = input().split(", ")
n = int(input())

all_items = {el: [] for el in categories}
all_quality = 0
all_quantity = 0

for _ in range(n):
    category, item_name, else_items = input().split(" - ")
    all_items[category].append(item_name)
    quantity, quality = [int(el.split(":")[1]) for el in else_items.split(";")]
    all_quantity += quantity
    all_quality += quality

print(f"Count of items: {all_quantity}")
print(f"Average quality: {(all_quality / len(categories)):.2f}")
[print(f"{key} -> {', '.join(value)}", ) for key, value in all_items.items()]
