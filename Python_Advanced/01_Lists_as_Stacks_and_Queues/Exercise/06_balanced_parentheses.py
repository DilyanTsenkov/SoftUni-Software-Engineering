parentheses = input()

balanced = True
opening = []

for p in parentheses:
    if p in "{[(":
        opening.append(p)
    else:
        if not opening:
            balanced = False
            break
        current = opening.pop()
        if p == "}" and current != "{":
            balanced = False
            break
        elif p == "]" and current != "[":
            balanced = False
            break
        elif p == ")" and current != "(":
            balanced = False
            break
if balanced:
    print("YES")
else:
    print("NO")
