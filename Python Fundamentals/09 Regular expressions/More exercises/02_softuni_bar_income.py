import re

total_income = 0

while True:
    input_string = input()
    if input_string == "end of shift":
        break

    regex = r"%(?P<name>[A-Z][a-z]+)%([^\!\|\$\%\.]+)?<(?P<product>[\w]+)>([^\!\|\$\%\.]+)?\|(?P<quantity>[\d]+)\|([^\!\|\$\%\.]+)?(?<=\||[^0-9])(?P<price>\d+(\.\d+)?)\$"

    input_string = re.finditer(regex, input_string)

    for data in input_string:
        d = data.groupdict()
        customer_name = d["name"]
        product = d["product"]
        total_price = float(d["price"]) * int((d["quantity"]))
        total_income += total_price
        print(f"{customer_name}: {product} - {total_price:.2f}")

print(f"Total income: {total_income:.2f}")
