chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input().lower()
holiday = input().lower()
flowers = chrysanthemums + roses + tulips
chrysanthemum_price = 3.75
rose_price = 4.5
tulip_price = 4.15
if season == "spring" or season == "summer":
    chrysanthemum_price = 2
    rose_price = 4.1
    tulip_price = 2.5
if holiday == "y":
    chrysanthemum_price *= 1.15
    rose_price *= 1.15
    tulip_price *= 1.15
bouquet_price = chrysanthemums * chrysanthemum_price + roses * rose_price + tulips * tulip_price
if tulips > 7 and season == "spring":
    bouquet_price *= 0.95
if roses >= 10 and season == "winter":
    bouquet_price *= 0.9
if flowers > 20:
    bouquet_price *= 0.8
arranging_bouquet = 2
result = bouquet_price + arranging_bouquet
print(f"{result:.2f}")
