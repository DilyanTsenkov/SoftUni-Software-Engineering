mackerel_price = float(input())
sprat_price = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = float(input())
bonito_price = mackerel_price * 1.6
horse_mackerel_price = sprat_price * 1.8
mussels_price = 7.5
money = bonito_kg * bonito_price + horse_mackerel_kg * horse_mackerel_price + mussels_kg * mussels_price
print(f'{money:.2f}')
