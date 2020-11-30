def decrypting(current_string, input_key):
    symbol = 0
    dec_text = ""
    for i in range(len(current_string)):
        new_letter = chr(ord(current_string[i]) - input_key[symbol])
        dec_text += new_letter
        symbol += 1
        if symbol == len(input_key):
            symbol = 0
    return dec_text


def formatted(text):
    start_flag = False
    for i in range(len(text)):
        if text[i] == "&":
            if start_flag:
                end_i_treasure = i
            else:
                start_i_treasure = i + 1
                start_flag = True
        elif text[i] == "<":
            start_i_coord = i + 1
        elif text[i] == ">":
            end_i_coord = i
    return text[start_i_treasure:end_i_treasure], text[start_i_coord:end_i_coord]


key = list(map(int, input().split()))
while True:
    string = input()
    if string == "find":
        break
    text = decrypting(string, key)
    treasure, coord = formatted(text)

    print(f"Found {treasure} at {coord}")
