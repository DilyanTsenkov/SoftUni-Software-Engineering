string = input()

list_of_sheep = string.split(", ")
list_of_sheep.reverse()
index = list_of_sheep.index("wolf")

if index == 0:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
