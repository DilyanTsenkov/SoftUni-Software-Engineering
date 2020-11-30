fire_list = input().split("#")
water = int(input())

RANGE_HIGH = range(81, 126)
RANGE_MED = range(51, 81)
RANGE_LOW = range(1, 51)

effort = 0
fire_level_print = []

for fire in fire_list:
    type_of_fire, fire_level = fire.split(" = ")
    fire_level = int(fire_level)

    is_valid = (type_of_fire == "High" and fire_level in RANGE_HIGH) or (
            type_of_fire == "Medium" and fire_level in RANGE_MED) or (type_of_fire == "Low" and fire_level in RANGE_LOW)

    if is_valid and water >= fire_level:
        water -= fire_level
        fire_level_print.append(fire_level)
        effort += fire_level

print("Cells:")

for fire_level in fire_level_print:
    print(f" - {fire_level}")

print(f"Effort: {(effort * 0.25):.2f}")
print(f"Total Fire: {effort}")