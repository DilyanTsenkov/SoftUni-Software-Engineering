word = ""
char = ""
c_counter = False
o_counter = False
n_counter = False
while True:
    char = input()
    if char == "End":
        break
    if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
        if char == "c":
            if c_counter:
                word += char
            c_counter = True
        elif char == "o":
            if o_counter:
                word += char
            o_counter = True
        elif char == "n":
            if n_counter:
                word += char
            n_counter = True
        else:
            word += char
    if c_counter == True and o_counter == True and n_counter == True:
        c_counter = False
        o_counter = False
        n_counter = False
        print(f"{word} ", end="")
        word = ''
