string_input = input()
n = int(input())


def string_repeat(string, repeat):
    repeated_string = ""
    for rep in range(n):
        repeated_string += string_input
    return repeated_string


print(string_repeat(string_input, n))
