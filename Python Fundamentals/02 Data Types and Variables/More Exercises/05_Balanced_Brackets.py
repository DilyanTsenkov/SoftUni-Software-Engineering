n_symbols = int(input())

counter = 0
result = "BALANCED"

for symbol in range(n_symbols):
    char = input()
    if char == "(":
        counter += 1
    if (char == ")" and counter != 1) or counter == 2:
        result = "UNBALANCED"
        break
    if char == ")" and counter == 1:
        result = "BALANCED"
        counter = 0

if counter == 1:
    print("UNBALANCED")
else:
    print(result)
