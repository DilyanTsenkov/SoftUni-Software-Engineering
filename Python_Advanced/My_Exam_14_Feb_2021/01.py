from collections import deque


def all_more_then_3(fireworks):
    if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks["Crossette Fireworks"] >= 3:
        return True


def printer(fireworks, fireworks_effects, explosive_power):
    if all_more_then_3(fireworks):
        print("Congrats! You made the perfect firework show!")
    else:
        print("Sorry. You can’t make the perfect firework show.")
    if fireworks_effects:
        print(f"Firework Effects left: {', '.join(str(el) for el in fireworks_effects)}")
    if explosive_power:
        print(f"Explosive Power left: {', '.join(str(el) for el in explosive_power)}")
    for key in fireworks:
        print(f"{key}: {fireworks[key]}")


fireworks_effects = deque(int(el) for el in input().split(", "))
explosive_power = [int(el) for el in input().split(", ")]
fireworks = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}
while fireworks_effects and explosive_power:
    while fireworks_effects and fireworks_effects[0] <= 0:
        fireworks_effects.popleft()
    if not fireworks_effects:
        break
    while explosive_power and explosive_power[-1] <= 0:
        explosive_power.pop()
    if not explosive_power:
        break
    sum_value = fireworks_effects[0] + explosive_power[-1]
    if sum_value % 3 == 0 and sum_value % 5 != 0:
        fireworks["Palm Fireworks"] += 1
        fireworks_effects.popleft()
        explosive_power.pop()
    elif sum_value % 5 == 0 and sum_value % 3 != 0:
        fireworks["Willow Fireworks"] += 1
        fireworks_effects.popleft()
        explosive_power.pop()
    elif sum_value % 5 == 0 and sum_value % 3 == 0:
        fireworks["Crossette Fireworks"] += 1
        fireworks_effects.popleft()
        explosive_power.pop()
    else:
        current_fireworks_effect = fireworks_effects.popleft()
        current_fireworks_effect -= 1
        fireworks_effects.append(current_fireworks_effect)
    if all_more_then_3(fireworks):
        break
printer(fireworks, fireworks_effects, explosive_power)
