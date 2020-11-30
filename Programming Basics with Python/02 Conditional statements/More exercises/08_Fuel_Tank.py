fuel = input().lower()
liters_in_tank = float(input())
if fuel == 'diesel' or fuel == 'gasoline' or fuel == 'gas':
    if liters_in_tank >= 25:
        print(f'You have enough {fuel}.')
    elif liters_in_tank < 25:
        print(f'Fill your tank with {fuel}!')
else:
    print('Invalid fuel!')
