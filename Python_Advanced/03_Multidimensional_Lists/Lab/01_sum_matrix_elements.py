rows, columns = (int(x) for x in input().split(", "))
matrix = [[int(el) for el in input().split(", ")] for row in range(rows)]
matrix_sum = (sum([n for i in matrix for n in i]))
print(matrix_sum)
print(matrix)
