def matrix_creator(rows):
    matrix = [input().split(", ") for _ in range(rows)]
    return matrix


rows = int(input())

matrix = matrix_creator(rows)
first_d = [matrix[i][i] for i in range(rows)]
second_d = [matrix[i][rows - i - 1] for i in range(rows)]

print(f"First diagonal: {', '.join(first_d)}. Sum: {sum([int(el) for el in first_d])}")
print(f"Second diagonal: {', '.join(list(str(el) for el in second_d))}. Sum: {sum([int(el) for el in second_d])}")
