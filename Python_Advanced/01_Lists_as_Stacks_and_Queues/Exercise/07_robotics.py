from collections import deque
from datetime import datetime, timedelta


def robot_extractor(fun_robots_data):
    robots_in_fun = []
    free_robots_in_fun = deque()
    for data in fun_robots_data:
        robot = {"name": (data.split("-"))[0], "working": int((data.split("-"))[1]), "can_start_at": time}
        robots_in_fun.append(robot)
        free_robots_in_fun.append(robot)
    return robots_in_fun, free_robots_in_fun


def add_products_on_line():
    result = deque()
    while True:
        product_in_fun = input()
        if product_in_fun == "End":
            break
        result.append(product_in_fun)
    return result


def free_robot_available(fun_free_robots, fun_product, fun_time):
    busy_robot = fun_free_robots.popleft()
    busy_robot["can_start_at"] = time + timedelta(seconds=busy_robot["working"])
    print(f"{busy_robot['name']} - {fun_product} [{fun_time.strftime('%H:%M:%S')}]")


def free_robot_not_available(fun_robots, fun_time, fun_free_robots, fun_products_line, fun_product):
    for robot in fun_robots:
        if fun_time >= robot["can_start_at"]:
            fun_free_robots.append(robot)
    if not fun_free_robots:
        fun_products_line.append(fun_product)
    return robots, time, free_robots, products_line, product


robots_data = input().split(";")
time = datetime.strptime(input(), "%H:%M:%S")
robots, free_robots = robot_extractor(robots_data)
products_line = add_products_on_line()
time += timedelta(seconds=1)
while len(products_line) > 0:
    product = products_line.popleft()
    if not free_robots:
        robots, time, free_robots, products_line, product = free_robot_not_available(robots, time, free_robots,
                                                                                     products_line, product)
    if free_robots:
        free_robot_available(free_robots, product, time)
    time += timedelta(seconds=1)
