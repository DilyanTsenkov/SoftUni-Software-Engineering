veg_price_per_kg = float(input())
fruit_price_per_kg = float(input())
vegetables_in_kg = int(input())
fruits_in_kg = int(input())
total = vegetables_in_kg * veg_price_per_kg + fruits_in_kg * fruit_price_per_kg
total_in_euro = total / 1.94
print(f'{total_in_euro:.2f}')
