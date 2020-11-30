def first_letter(r_string, first_i, num):
    if r_string[first_index].isupper():
        num /= (ord(r_string[first_i]) - 64)
    elif r_string[first_index].islower():
        num *= (ord(r_string[first_i]) - 96)
    return num


def second_letter(r_string, second_i, num):
    if r_string[second_i].isupper():
        num -= (ord(r_string[second_i]) - 64)
    elif r_string[second_i].islower():
        num += (ord(r_string[second_i]) - 96)
    return num


received_string = input()
number = ""
result = 0

for n in range(len(received_string)):
    if received_string[n] == " ":
        continue
    if received_string[n].isalpha():
        if number == "":
            first_index = n
        else:
            second_index = n
            number = first_letter(received_string, first_index, float(number))
            number = second_letter(received_string, second_index, float(number))
            result += number
            number = ""
    elif received_string[n].isdigit():
        number += received_string[n]

print(f"{result:.2f}")
