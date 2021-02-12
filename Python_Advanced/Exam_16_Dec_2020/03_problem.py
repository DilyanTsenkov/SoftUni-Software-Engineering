def get_magic_triangle(n):
    triangle = []
    for c in range(0, n):
        row = []
        for r in range(c + 1):
            row.append(1)
        triangle.append(row)

    for i in range(1, n):
        row = triangle[i]
        additional = 0
        for k in range(1, len(row) - 1):
            row_index = i - 1
            col_index = i - i + additional
            row[k] = triangle[row_index][col_index] + triangle[row_index][col_index + 1]
            additional += 1
    return triangle


get_magic_triangle(6)
