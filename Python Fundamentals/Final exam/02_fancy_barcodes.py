import re

count_of_barcodes = int(input())

for n in range(count_of_barcodes):
    product_group = ""
    barcode = input()
    regex = r"@[#]+[A-Z](?P<product>[A-Za-z0-9]{4,})[A-Z]@[#]+"
    code = re.findall(regex, barcode)
    if code:
        code = "".join(code)
        for symbol in code:
            if symbol.isdigit():
                product_group += symbol
        if product_group == "":
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
