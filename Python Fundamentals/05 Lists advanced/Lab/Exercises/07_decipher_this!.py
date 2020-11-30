message = input().split()

message = [chr(int(el[:3])) + el[3:] if el[2].isdigit() else chr(int(el[:2])) + el[2:] for el in message]

final_message = []

for el in message:
    temp_list = [el[i] for i in range(len(el))]
    temp_list[1], temp_list[-1] = temp_list[-1], temp_list[1]
    final_message.append("".join(temp_list))
    temp_list.clear()

print(" ".join(final_message))