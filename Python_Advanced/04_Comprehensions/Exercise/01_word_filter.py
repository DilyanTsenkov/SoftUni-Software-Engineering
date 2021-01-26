string_list = input().split()
string_list = [print(el) for el in string_list if len(el) % 2 == 0]
