received_string = input().upper()

string_to_print = ""
index = 0

while len(received_string) > 0:
    if received_string[index].isdigit():
        if index + 1 < len(received_string):
            if received_string[index + 1].isdigit():
                number = received_string[index] + received_string[index + 1]
                number = int(number)
                string_to_print += (received_string[:index].upper()) * int(number)
                received_string = received_string[index + 2:]
                index = -1
            else:
                if int(received_string[index]) == 0:
                    received_string = received_string[index + 1:]
                    index = -1
                else:
                    string_to_print += (received_string[:index].upper()) * int(received_string[index])
                    received_string = received_string[index + 1:]
                    index = -1
        else:
            if int(received_string[index]) == 0:
                received_string = received_string[index + 1:]
                index = -1
            else:
                string_to_print += (received_string[:index].upper()) * int(received_string[index])
                received_string = received_string[index + 1:]
                index = -1
    index += 1

print(f"Unique symbols used: {len(set(string_to_print))}")
print(string_to_print)