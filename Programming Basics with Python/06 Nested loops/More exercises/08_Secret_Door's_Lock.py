up_100 = int(input())
up_10 = int(input())
up_1 = int(input())
for number_100 in range(1, up_100 + 1):
    for number_10 in range(2, up_10 + 1):
        if number_10 > 7 or ((number_10 > 2) and (number_10 % 2 == 0)):
            continue
        for number_1 in range(1, up_1 + 1):
            if number_100 % 2 == 0 and number_1 % 2 == 0:
                print(number_100, number_10, number_1)
#-----------------------------------------------------------------------------
up_100 = int(input())
up_10 = int(input())
up_1 = int(input())
for number_100 in range(1, up_100 + 1):
    for number_10 in range(2, up_10 + 1):
        if number_10 > 7:
            continue
        for number_1 in range(1, up_1 + 1):
            if number_100 % 2 == 0 and number_1 % 2 == 0 and ((number_10 == 2) or (number_10 % 2 == 1)):
                print(number_100, number_10, number_1)