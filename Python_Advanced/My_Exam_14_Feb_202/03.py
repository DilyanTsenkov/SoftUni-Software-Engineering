from collections import deque


def stock_availability(*args):
    boxes = deque(args[0])
    delivery_or_sell = args[1]
    if delivery_or_sell == "delivery":
        new_boxes = args[2::]
        for box in new_boxes:
            boxes.append(box)
    elif delivery_or_sell == "sell":
        if len(args) > 2:
            parameter = args[2::]
            if type(parameter[0]) == int:
                for _ in range(args[2]):
                    boxes.popleft()
            else:
                for el in parameter:
                    boxes = [box for box in boxes if box != el]
        else:
            boxes.popleft()
    return list(boxes)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
