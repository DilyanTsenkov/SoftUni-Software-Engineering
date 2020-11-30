snowballs = int(input())

snowball_value = 0
highest_snowball_value = 0
result = ""

for snowball in range(snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow // snowball_time) ** snowball_quality
    if snowball_value > highest_snowball_value:
        highest_snowball_value = snowball_value
        result = f"{snowball_snow} : {snowball_time} = {highest_snowball_value} ({snowball_quality})"

print(result)