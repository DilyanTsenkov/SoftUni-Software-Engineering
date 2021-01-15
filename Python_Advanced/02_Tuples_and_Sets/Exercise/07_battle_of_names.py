n = int(input())

even = set()
odd = set()

for number in range(1, n + 1):
    name = input()
    ascii_sum = 0

    for ch in name:
        ascii_sum += ord(ch)
    result = ascii_sum // number

    if result % 2 == 0:
        even.add(result)
    else:
        odd.add(result)

odd_sum = sum(odd)
even_sum = sum(even)

union = odd.union(even)
different = odd.difference(even)
symmetric = odd.symmetric_difference(even)

if odd_sum == even_sum:
    print(*union, sep=", ")
elif odd_sum > even_sum:
    print(*different, sep=", ")
else:
    print(*symmetric, sep=", ")
