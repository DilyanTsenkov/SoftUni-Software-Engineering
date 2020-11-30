year = int(input())

happyYear = year + 1
a = str(happyYear)
flag_new_year = False

while flag_new_year == False:
    flag = False
    for i in range(len(a)):
        if len(a) == 1:
            flag_new_year = True
        if flag:
            break
        for j in range(i + 1, len(a)):
            if (a[i] == a[j]):
                i = 0
                j = 0
                happyYear += 1
                a = str(happyYear)
                flag = True
                break
            if j == len(a) - 1 and i == j - 1:
                flag = True
                flag_new_year = True
                break

print(happyYear)

