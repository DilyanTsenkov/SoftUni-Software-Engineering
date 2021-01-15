n = int(input())

guest_list = set()
guest_arrived = set()

for _ in range(n):
    guest = input()
    guest_list.add(guest)

while True:
    arrived = input()
    if arrived == "END":
        break
    guest_arrived.add(arrived)

not_arrived = set(guest_list).difference(guest_arrived)

vip = []
regular = []

for guest in not_arrived:
    if guest[0].isdigit():
        vip.append(guest)
    else:
        regular.append(guest)

vip.sort()
regular.sort()

print(len(not_arrived))
for guest in vip:
    print(guest)
for guest in regular:
    print(guest)

