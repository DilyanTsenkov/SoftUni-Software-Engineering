def combination(names, chairs, comb_counter=[]):
    if len(comb_counter) == chairs:
        print(", ".join(comb_counter))
        return
    for i in range(len(names)):
        current_name = names[i]
        comb_counter.append(current_name)
        combination(names[i + 1:], chairs, comb_counter)
        comb_counter.pop()


names = input().split(", ")
chairs = int(input())
combination(names, chairs)

# from itertools import combinations
#
# names = input().split(", ")
# chairs = int(input())
#
# print(*[f"{', '.join(el)}" for el in list(combinations(names, chairs))], sep="\n")
