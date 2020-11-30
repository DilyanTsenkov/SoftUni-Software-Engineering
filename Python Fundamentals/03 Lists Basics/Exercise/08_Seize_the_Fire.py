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



# fire = input()
# water = int(input())
# fire_list = fire.split("#")
# new_fire_List = []
# effort = 0
# for i in fire_list:
#     new_fire_List.append(i.split(' = '))
# print("Cells:")
# for i in range(len(new_fire_List)):
#     fire_type = new_fire_List[i][0]
#     fire_level = int(new_fire_List[i][1])
#     if fire_type == "High":
#         if 81 <= int(new_fire_List[i][1]) <= 125:
#             if water >= fire_level:
#                 water -= fire_level
#                 print(f" - {fire_level}")
#                 effort += fire_level
#     if fire_type == "Medium":
#         if 51 <= fire_level <= 80:
#             if water >= fire_level:
#                 water -= fire_level
#                 print(f" - {fire_level}")
#                 effort += fire_level
#     if fire_type == "Low":
#         if 1 <= fire_level <= 50:
#             if water >= fire_level:
#                 water -= fire_level
#                 print(f" - {fire_level}")
#                 effort += fire_level
# print(f"Effort: {(effort * 0.25):.2f}")
# print(f"Total Fire: {effort}")


# fire_list = input().split("#")
# water = int(input())
# RANGE_HIGH = range(81, 126)
# RANGE_MED = range(51, 81)
# RANGE_LOW = range(1, 51)
# effort = 0
# fire_level_print = []
# for fire in fire_list:
#     type_of_fire, fire_level = fire.split(" = ")
#     fire_level = int(fire_level)
#     if type_of_fire == "High" and fire_level in RANGE_HIGH:
#         if water >= fire_level:
#             water -= fire_level
#             fire_level_print.append(fire_level)
#             effort += fire_level
#     elif type_of_fire == "Medium" and fire_level in RANGE_MED:
#         if water >= fire_level:
#             water -= fire_level
#             fire_level_print.append(fire_level)
#             effort += fire_level
#     elif type_of_fire == "Low" and fire_level in RANGE_LOW:
#         if water >= fire_level:
#             water -= fire_level
#             fire_level_print.append(fire_level)
#             effort += fire_level
# print("Cells:")
# for fire_level in fire_level_print:
#     print(f" - {fire_level}")
# print(f"Effort: {(effort * 0.25):.2f}")
# print(f"Total Fire: {effort}")
