text = input()

stack = []

for n in range(len(text)):
    if text[n] == "(":
        stack.append(n)
    elif text[n] == ")":
        start = stack.pop()
        print(text[start:n + 1])
