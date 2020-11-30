n = int(input())

capacity = 255
water = 0

for pour in range(n):
    liters = int(input())
    if water + liters > capacity:
        print("Insufficient capacity!")
    else:
        water += liters

print(water)
