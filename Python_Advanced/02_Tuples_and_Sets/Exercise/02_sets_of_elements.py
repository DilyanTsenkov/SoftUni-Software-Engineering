n, m = input().split()

set_n = set()
set_m = set()

for _ in range(int(n)):
    number = input()
    set_n.add(number)

for _ in range(int(m)):
    number = input()
    set_m.add(number)

unique_el = set_n.intersection(set_m)

print("\n".join(unique_el))
