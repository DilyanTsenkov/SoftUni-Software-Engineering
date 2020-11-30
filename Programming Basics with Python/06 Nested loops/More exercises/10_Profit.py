one_lv = int(input())
two_lv = int(input())
five_lv = int(input())
money = int(input())
for one in range(0, one_lv + 1):
    for two in range(0, two_lv + 1):
        for five in range(0, five_lv + 1):
            if five * 5 + two * 2 + one == money:
                print(f"{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {money} lv.")