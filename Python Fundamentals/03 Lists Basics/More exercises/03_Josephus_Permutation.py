elements = input().split(" ")
number = int(input())

new_elements_list = []
counter = 0

while len(elements) != 0:

    for i in range(len(elements)):
        counter += 1

        if counter % number == 0:
            new_elements_list.append(elements[i])
            elements[i] = None

    elements = [i for i in elements if i]

print("[" + ",".join(new_elements_list) + "]")