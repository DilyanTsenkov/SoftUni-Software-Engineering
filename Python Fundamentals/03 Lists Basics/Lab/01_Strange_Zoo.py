tail = input()
body = input()
head = input()

meerkats_list = [tail, body, head]
meerkats_list[0], meerkats_list[2] = meerkats_list[2], meerkats_list[0]

print(meerkats_list)
