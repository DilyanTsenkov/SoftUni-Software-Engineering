budget = float(input())
flour_price = float(input())

egg_price = flour_price * 0.75
milk_price = flour_price * 1.25 * 0.25
cozonac_price = flour_price + egg_price + milk_price
cozonacs = 0
colored_eggs = 0

while budget >= cozonac_price:
    cozonacs += 1
    colored_eggs += 3

    if cozonacs % 3 == 0:
        colored_eggs -= (cozonacs - 2)
    budget -= cozonac_price

print(f"You made {cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")