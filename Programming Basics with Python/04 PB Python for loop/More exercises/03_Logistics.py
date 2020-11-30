loads = int(input())
minibus_loads = 0
truck_loads = 0
train_loads = 0
total_loads = 0
for load in range(0, loads):
    input_load = int(input())
    if input_load <= 3:
        minibus_loads += input_load
        total_loads += input_load
    elif 4 <= input_load <= 11:
        truck_loads += input_load
        total_loads += input_load
    elif input_load >= 12:
        train_loads += input_load
        total_loads += input_load
average_price = (minibus_loads * 200 + truck_loads * 175 + train_loads * 120) / total_loads
minibus_percent = minibus_loads / total_loads * 100
truck_percent = truck_loads / total_loads * 100
train_percent = 100 - minibus_percent - truck_percent
print(f'{average_price:.2f}')
print(f'{minibus_percent:.2f}%')
print(f'{truck_percent:.2f}%')
print(f'{train_percent:.2f}%')
