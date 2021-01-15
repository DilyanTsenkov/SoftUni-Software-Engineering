from collections import deque

bullet_price = int(input())
gun_barrel = int(input())
bullets = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
value = int(input())

reload = True
costs = 0

while bullets:
    for _ in range(gun_barrel):
        if not bullets or not locks:
            reload = False
            break
        lock = locks.popleft()
        if lock < bullets.pop():
            print("Ping!")
            locks.appendleft(lock)
        else:
            print("Bang!")
        costs += bullet_price
    if bullets and reload:
        print("Reloading!")
    if not locks:
        print(f"{len(bullets)} bullets left. Earned ${value - costs}")
        break
    if not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")