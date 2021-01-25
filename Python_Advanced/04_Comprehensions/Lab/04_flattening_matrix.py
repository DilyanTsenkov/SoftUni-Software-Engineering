def matrix_creator(rows):
    matrix = [input().split(", ") for _ in range(rows)]
    return matrix


rows = int(input())
matrix = matrix_creator(rows)

print([int(col) for row in matrix for col in row])
