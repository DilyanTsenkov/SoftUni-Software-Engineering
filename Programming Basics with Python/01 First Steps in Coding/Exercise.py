# -----------------------------------------------08. Fish Tank
length = int(input())
width = int(input())
high = int(input())
percent_volume = float(input())
full_volume = length * width * high
water_volume = full_volume - full_volume * percent_volume / 100
liters = water_volume / 1000
print(liters)
# -----------------------------------------------07. Fruit Market
price_strawberry = float(input())
kg_bananas = float(input())
kg_oranges = float(input())
kg_raspberries = float(input())
kg_strawberry = float(input())
price_raspberries = price_strawberry / 2
price_oranges = price_raspberries - price_raspberries * 0.4
price_bananas = price_raspberries - price_raspberries * 0.8
money = price_strawberry * kg_strawberry + price_raspberries * kg_raspberries + \
        price_bananas * kg_bananas + price_oranges * kg_oranges
print(money)
# -----------------------------------------------06. Charity Campaign
days = int(input())
cooker = int(input())
cakes = int(input())
waffle = int(input())
pancakes = int(input())
price_cakes = 45
price_waffle = 5.80
price_pancakes = 3.20
profit_by_cooker_per_day = (cakes * price_cakes + waffle * price_waffle + pancakes * price_pancakes)
profit_all_cookers_per_day = profit_by_cooker_per_day * cooker
all_days_profit = profit_all_cookers_per_day * days
costs = all_days_profit / 8
charity = all_days_profit - costs
print(charity)
# -----------------------------------------------05. Birthday party
rent = int(input())
cake = rent * 0.20
drinks = cake - (cake * 0.45)
animator = rent / 3
budget = rent + cake + drinks + animator
print(budget)
# -----------------------------------------------04. Vacation books list
pages = int(input())
pages_per_hour = int(input())
days = int(input())
needed_hours = pages / pages_per_hour
needed_days = needed_hours / days
print(needed_days)
# -----------------------------------------------03. Deposit Calculator
deposit = float(input())
term = int(input())
dividend = float(input())
my_money = deposit + term * ((deposit * dividend / 100) / 12)
print(my_money)
# -----------------------------------------------02. Radians to Degrees
import math

radians = float(input())
degrees = math.floor(radians * 180 / math.pi)
print(degrees)
# -----------------------------------------------01. USD to BGN
usd = float(input())
exchange = 1.79549
bgn = usd * exchange
print(bgn)
