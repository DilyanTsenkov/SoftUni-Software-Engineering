from itertools import permutations


def possible_permutations(perm):
    p = permutations(perm)
    for i in p:
        i = list(i)
        yield i


[print(n) for n in possible_permutations([1, 2, 3])]
