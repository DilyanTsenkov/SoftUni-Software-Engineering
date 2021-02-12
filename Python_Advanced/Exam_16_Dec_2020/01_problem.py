from collections import deque

males = deque(int(el) for el in input().split())
females = deque(int(el) for el in input().split())

matches = 0
while males and females:
    while males and males[-1] <= 0:
        males.pop()
    if not males:
        break
    while females and females[0] <= 0:
        females.popleft()
    if not females:
        break
    while males and males[-1] % 25 == 0:
        males.pop()
        if not males:
            break
        males.pop()
    if not males:
        break
    while females and females[-1] % 25 == 0:
        females.popleft()
        if not females:
            break
        females.popleft()
    if not females:
        break
    if males[-1] == females[0]:
        males.pop()
        females.popleft()
        matches += 1
    else:
        male = males.pop()
        male -= 2
        males.append(male)
        females.popleft()

males = [str(male) for male in males][::-1]
females = [str(female) for female in females]

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(males)}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join(females)}")
else:
    print("Females left: none")
