from collections import deque

countries = input().split(", ")
capitals = deque(input().split(", "))
dictionary = {country: capitals.popleft() for country in countries}

for key, value in dictionary.items():
    print(f"{key} -> {value}")
