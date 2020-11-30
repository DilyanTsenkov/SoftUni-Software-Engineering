numbers = input().split(", ")
numbers = [int(el) for el in numbers]

max_element_in_numbers = max(numbers)

for i in range(10, max_element_in_numbers + 10, 10):
    my_list = list(filter((lambda x: i - 10 < x <= i), numbers))
    print(f"Group of {i}'s: {my_list}")
    my_list.clear()