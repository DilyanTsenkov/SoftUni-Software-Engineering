def fibonacci():
    current = -1
    next_num = 1
    while True:
        number = current + next_num
        current = next_num
        next_num = number
        yield number


generator = fibonacci()
for i in range(9):
    print(next(generator))
