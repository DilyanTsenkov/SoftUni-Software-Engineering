from collections import deque

green_light = int(input())
yellow_light = int(input())

counter = 0
time_to_quit = False
cars = deque()

while not time_to_quit:
    while True:
        car = input()
        if car == "END":
            print(f"Everyone is safe.")
            print(f"{counter} total cars passed the crossroads.")
            time_to_quit = True
            break
        if car == "green":
            green = green_light
            yellow = yellow_light
            break
        cars.append(car)
    while green != 0:
        if not cars:
            break
        passing_car = cars.popleft()
        passing_car_parts = deque(passing_car)
        while passing_car_parts:
            if time_to_quit:
                break
            char = passing_car_parts.popleft()
            green -= 1
            if green == 0 and passing_car_parts:
                while passing_car_parts:
                    char = passing_car_parts.popleft()
                    yellow -= 1
                    if yellow == -1:
                        print(f"A crash happened!")
                        print(f"{passing_car} was hit at {char}.")
                        time_to_quit = True
                        break
        counter += 1
