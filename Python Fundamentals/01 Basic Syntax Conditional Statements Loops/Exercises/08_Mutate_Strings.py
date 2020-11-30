first_string = input()
second_string = input()

counter_one = 1
counter_two = 0

for i in second_string:
    string_one = first_string[counter_one:]
    string_two = second_string[:counter_one]
    string_three = string_two + string_one
    counter_one += 1
    f1 = first_string[counter_two]
    f2 = second_string[counter_two]
    counter_two += 1
    if f1 != f2:
        print(string_three)


