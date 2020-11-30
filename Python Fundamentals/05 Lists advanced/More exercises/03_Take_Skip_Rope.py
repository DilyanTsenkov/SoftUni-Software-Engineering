encrypted_message = list(input())

digit_in_message = list(filter(lambda el: el.isdigit(), encrypted_message))

digit_in_message = [int(el) for el in digit_in_message]
take_list = [digit_in_message[el] for el in range(len(digit_in_message)) if el % 2 == 0]
skip_list = [digit_in_message[el] for el in range(len(digit_in_message)) if int(el) % 2 != 0]

char_in_message = list(filter(lambda el: not el.isdigit(), encrypted_message))

result = []
for i in range(len(take_list)):
    result += char_in_message[:take_list[i]]
    char_in_message = char_in_message[take_list[i]:]
    char_in_message = char_in_message[skip_list[i]:]

print("".join(result))
