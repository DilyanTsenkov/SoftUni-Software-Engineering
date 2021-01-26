rows, cols = [int(x) for x in input().split()]

matrix = [[chr(97 + row) + chr(97 + row + col) + chr(97 + row) for col in range(cols)] for row in range(rows)]

[print(" ".join(row)) for row in matrix]
