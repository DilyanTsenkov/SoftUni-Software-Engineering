from collections import deque

cups = deque(int(x) for x in input().split())
bottles = deque((int(x) for x in input().split()))

wasted_water = 0
remaining = ""

while True:
    bottle = bottles.pop()
    cup = cups.popleft()
    if bottle >= cup:
        wasted_water += bottle - cup
    else:
        while True:
            cup = cup - bottle
            if cup <= 0:
                wasted_water += abs(cup)
                break
            bottle = bottles.pop()
    if not bottles:
        for el in cups:
            remaining += str(el) + " "
        print(f"Cups: {remaining.strip()}")
        print(f"Wasted litters of water: {wasted_water}")
        break
    if not cups:
        for el in bottles:
            remaining += str(el) + " "
        print(f"Bottles: {remaining.strip()}")
        print(f"Wasted litters of water: {wasted_water}")
        break

