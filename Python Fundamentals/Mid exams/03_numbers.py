integers = list(map(int, input().split()))

average = sum(integers) / len(integers)
top_5 = []

for i in range(len(integers)):
    if integers[i] > average:
        top_5.append(integers[i])

top_5.sort(reverse=True)
top_5 = top_5[:5]
top_5 = [str(top_5[i]) for i in range(len(top_5))]

if len(top_5) == 0:
    print("No")
else:
    print(" ".join(top_5))
