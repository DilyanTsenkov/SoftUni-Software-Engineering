number = int(input())

counter = 0

for i in range(2, number + 1):
    if number % i == 0:
        counter += 1
if counter == 1:
    print("True")
else:
    print("False")
