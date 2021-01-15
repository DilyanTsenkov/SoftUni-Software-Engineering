phone_book = {}

while True:
    receive = input()
    if receive.isdigit():
        break
    name, phone = receive.split("-")
    phone_book[name] = phone

for _ in range(int(receive)):
    call = input()
    if call in phone_book:
        print(f"{call} -> {phone_book[call]}")
    else:
        print(f"Contact {call} does not exist.")
