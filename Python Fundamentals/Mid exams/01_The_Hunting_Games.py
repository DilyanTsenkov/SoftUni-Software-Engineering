adventure_days = int(input())
players = int(input())
group_energy = float(input())
water_per_day_for_person = float(input())
food_per_day_for_person = float(input())

water_supplies = players * water_per_day_for_person * adventure_days
food_supplies = players * food_per_day_for_person * adventure_days
no_energy_flag = False

for day in range(1, adventure_days + 1):

    energy_loss = float(input())
    group_energy -= energy_loss
    if group_energy <= 0:
        no_energy_flag = True
        break
    if day % 2 == 0:
        group_energy *= 1.05
        water_supplies *= 0.7
    if day % 3 == 0:
        group_energy *= 1.10
        food_supplies -= (food_supplies / players)

if no_energy_flag:
    print(f"You will run out of energy. You will be left with {food_supplies:.2f} food and {water_supplies:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
