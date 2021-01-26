receive = [el.split()[::-1] for el in input().split("|")]
receive = [el for row in receive for el in row]
receive.reverse()
print(*receive)
