def combination(text, index=0):
    if index == len(text):
        print("".join(text))
        return

    for i in range(index, len(text)):
        text[index], text[i] = text[i], text[index]
        combination(text, index + 1)
        text[index], text[i] = text[i], text[index]


text = list(input())
combination(text)

# from itertools import permutations
#
# text = list(input())
# print(*[f"{''.join(el)}" for el in list(permutations(text))], sep="\n")
