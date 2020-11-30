n = int(input())

for _ in range(n):
    received_string = input()
    for i in range(len(received_string)):
        if received_string[i] == "@":
            start_i_name = i + 1
        elif received_string[i] == "|":
            end_i_name = i
        elif received_string[i] == "#":
            start_i_age = i + 1
        elif received_string[i] == "*":
            end_i_age = i
    print(f"{received_string[start_i_name:end_i_name]} is {received_string[start_i_age:end_i_age]} years old.")
