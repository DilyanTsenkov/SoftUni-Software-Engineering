def squares(n):
    for number in range(1, n + 1):
        yield number * number


print(list(squares(5)))
