def racers(count):
    cars = {}
    for n in range(count):
        car, mileage, fuel = input().split("|")
        mileage = int(mileage)
        fuel = int(fuel)
        cars[car] = [mileage, fuel]
    return cars


def drive(car_racers, car, distance, fuel):
    if car_racers[car][1] < fuel:
        print("Not enough fuel to make that ride")
    else:
        car_racers[car][1] -= fuel
        car_racers[car][0] += distance
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if car_racers[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            car_racers.pop(car)
    return car_racers


def refuel(car_racers, car, fuel):
    car_racers[car][1] += fuel
    if car_racers[car][1] > 75:
        refueled = 75 - (car_racers[car][1] - fuel)
        car_racers[car][1] = 75
    else:
        refueled = fuel
    print(f"{car} refueled with {refueled} liters")
    return car_racers


def revert(car_racers, car, kilometers):
    car_racers[car][0] -= kilometers
    if car_racers[car][0] < 10000:
        car_racers[car][0] = 10000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")
    return car_racers


racers_count = int(input())
car_racers = racers(racers_count)

while True:
    command = input()
    if command == "Stop":
        break

    command = command.split(" : ")
    action = command[0]
    if action == "Drive":
        car_racers = drive(car_racers, command[1], int(command[2]), int(command[3]))
    elif action == "Refuel":
        car_racers = refuel(car_racers, command[1], int(command[2]))
    elif action == "Revert":
        car_racers = revert(car_racers, command[1], int(command[2]))

car_racers = dict(sorted(car_racers.items(), key=lambda x: (-x[1][0], x[0])))

for key, value in car_racers.items():
    print(f"{key} -> Mileage: {car_racers[key][0]} kms, Fuel in the tank: {car_racers[key][1]} lt.")
