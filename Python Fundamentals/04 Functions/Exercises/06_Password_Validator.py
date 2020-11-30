def validator(parameter):
    valid = True
    if not 6 <= len(parameter) <= 10:
        print("Password must be between 6 and 10 characters")
        valid = False
    if not parameter.isalnum():
        print("Password must consist only of letters and digits")
        valid = False
    digit_counter = 0
    for i in parameter:
        if i.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        valid = False
    if valid:
        print("Password is valid")


password = input()

validator(password)
