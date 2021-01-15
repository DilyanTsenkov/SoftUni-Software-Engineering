n = int(input())

records = set()

for _ in range(n):
    action, number = input().split(", ")
    if action == "IN":
        records.add(number)
    elif action == "OUT":
        records.remove(number)

if records:
    print("\n".join(records))
else:
    print("Parking Lot is Empty")
