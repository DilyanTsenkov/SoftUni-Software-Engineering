from collections import deque


def male_0(males):
    while males and males[-1] <= 0:
        males.pop()
    return males


def female_0(females):
    while females and females[0] <= 0:
        females.popleft()
    return females


def male_25(males):
    while males and males[-1] % 25 == 0:
        males.pop()
        if not males:
            break
        males.pop()
    return males


def female_25(females):
    while females and females[0] % 25 == 0:
        females.popleft()
        if not females:
            break
        females.popleft()
    return females


def male_female_compare(males, females, matches):
    if males[-1] == females[0]:
        males.pop()
        females.popleft()
        matches += 1
    else:
        male = males.pop()
        male -= 2
        males.append(male)
        females.popleft()
    return males, females, matches


def printer(males, females, matches):
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


males = [int(el) for el in input().split()]
females = deque(int(el) for el in input().split())
matches = 0
while males and females:
    males = male_0(males)
    if not males:
        break
    females = female_0(females)
    if not females:
        break
    males = male_25(males)
    if not males:
        break
    females = female_25(females)
    if not females:
        break
    males, females, matches = male_female_compare(males, females, matches)
printer(males, females, matches)
