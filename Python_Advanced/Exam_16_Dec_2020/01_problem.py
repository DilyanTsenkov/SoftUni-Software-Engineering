from collections import deque


def female_male_0(females_males):
    while females_males and females_males[-1] <= 0:
        females_males.pop()
    return females_males


def female_male_25(females_males):
    while females_males and females_males[-1] % 25 == 0:
        females_males.pop()
        if not females_males:
            break
        females_males.pop()
    return females_males


def no_males_or_females(females_males):
    if not females_males:
        return True


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


males = deque(int(el) for el in input().split())
females = deque(int(el) for el in input().split())
matches = 0
while males and females:
    males = female_male_0(males)
    if no_males_or_females(males):
        break
    females = female_male_0(females)
    if no_males_or_females(females):
        break
    female_male_25(males)
    if no_males_or_females(males):
        break
    female_male_25(females)
    if no_males_or_females(females):
        break
    males, females, matches = male_female_compare(males, females, matches)
printer(males, females, matches)