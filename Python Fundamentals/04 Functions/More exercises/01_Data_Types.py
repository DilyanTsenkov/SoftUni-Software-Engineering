def input_data_type(first_line, second_line):
    result = None
    if first_line == "int":
        result = 2 * int(second_line)
    elif first_line == "real":
        result = 1.5 * float(second_line)
        result = f"{result:.2f}"
    elif first_line == "string":
        result = "$" + second_line + "$"
    return result


first_line_input = input()
second_line_input = input()

print(input_data_type(first_line_input, second_line_input))
