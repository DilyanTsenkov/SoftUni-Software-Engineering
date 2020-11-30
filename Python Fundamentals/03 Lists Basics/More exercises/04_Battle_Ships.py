rows_of_the_field = int(input())

row_list = []

for row_of_the_field in range(rows_of_the_field):
    row = input()
    row_list.append(row)

attacked_squares = input().split(" ")
destroyed = 0
row_number = 0

for element in range(len(row_list)):
    col_number = 0
    for i in row_list[element]:
        if i == " ":
            continue
        else:
            if int(i) > 0:
                ship = int(i)
                for attack in range(len(attacked_squares)):
                    if int(attacked_squares[attack][0]) == row_number and int(
                            attacked_squares[attack][2]) == col_number and ship != 0:
                        ship -= 1
                        if ship == 0:
                            destroyed += 1
            col_number += 1
    row_number += 1

print(destroyed)
