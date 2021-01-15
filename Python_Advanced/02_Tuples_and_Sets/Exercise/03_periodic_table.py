input_lines = int(input())

elements = set()

for _ in range(input_lines):
    chemical_compounds = input().split()
    for el in chemical_compounds:
        elements.add(el)

print("\n".join(elements))
