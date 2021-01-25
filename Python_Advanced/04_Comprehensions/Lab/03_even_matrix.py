def matrix_creator(rows):
    matrix = []
    for _ in range(rows):
        line = [int(el) for el in input().split(", ")]
        matrix.append(line)
    return matrix


rows = int(input())
matrix = matrix_creator(rows)

for i in range (len(matrix)):
    new_row = [el for el in matrix[i] if el % 2 == 0]
    matrix[i] = new_row
print(matrix)
