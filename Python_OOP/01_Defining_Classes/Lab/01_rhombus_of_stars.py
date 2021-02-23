def draw_row(symbol_multiplier, symbol, space_multiplier=0):
    first_part = " " * space_multiplier + symbol
    second_part = (" " + symbol) * symbol_multiplier
    return f"{first_part}{second_part}"


def print_row(symbol_multiplier, symbol, space_multiplier=0):
    print(draw_row(symbol_multiplier, symbol, space_multiplier))


def draw_rhombus(n):
    for i in range(n - 1, -1, -1):
        print_row(n - i - 1, "*", i)
    for i in range(1, n):
        print_row(n - i - 1, "*", i)


# for triangle:
# def draw_triangle(n):
#     for i in range(n - 1):
#         print_row(i, "+")
#     for i in range(n - 2, -2, -1):
#         print_row(i + 1, "+")


n = int(input())
draw_rhombus(n)
# draw_triangle(n)
