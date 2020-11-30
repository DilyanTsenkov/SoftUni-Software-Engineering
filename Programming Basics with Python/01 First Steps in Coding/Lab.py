# ------------------------------------------01. Hello SoftUni
print('Hello SoftUni')
# ------------------------------------------02. Nums 1...10
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
# ------------------------------------------03. Square Area
a = int(input())
area = a * a
print(area)
# ------------------------------------------04. Inches to Centimeters
inch = float(input())
cm = inch * 2.54
print(cm)
# ------------------------------------------05. Greeting by Name
name = input()
print(f'Hello, {name}!')
# ------------------------------------------06. Concatenate Data
first_name = input()
last_name = input()
age = int(input())
town = input()
print(f'You are {first_name} {last_name}, a {age}-years old person from {town}.')
# ------------------------------------------07. Projects Creation
arh_name = input()
projects = int(input())
time = projects * 3
print(f'The architect {arh_name} will need {time} hours to complete {projects} project/s.')
# ------------------------------------------08. Pet Shop
dogs = int(input())
animals = int(input())
dog_food = 2.5 * dogs
animal_food = 4 * animals
print(f'{dog_food + animal_food} lv.')
# ------------------------------------------09. Yard Greening
yard = float(input())
sq_meter = 7.61
price = yard * sq_meter
discount = price * 0.18
total_price = price - discount
print(f'The final price is: {total_price} lv.')
print(f'The discount is: {discount} lv.')
