bottles = int(input())
detergent = bottles * 750
wash_counter = 0
dish_counter = 0
pot_counter = 0
while detergent >= 0:
    wash = input()
    if wash == "End":
        break
    wash_counter += 1
    if wash_counter == 3:
        detergent -= 15 * (int(wash))
        wash_counter = 0
        pot_counter += int(wash)
    else:
        detergent -= 5 * (int(wash))
        dish_counter += int(wash)
if detergent < 0:
    print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
else:
    print(
        f"Detergent was enough!\n{dish_counter} dishes and {pot_counter} pots were washed.\nLeftover detergent {detergent} ml.")
