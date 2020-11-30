miner = {}

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())

    if resource not in miner:
        miner[resource] = quantity
    else:
        miner[resource] += quantity

for resource, quantity in miner.items():
    print(f"{resource} -> {quantity}")
