control_number = int(input())
counter = 0
password = "No!"
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d and control_number == a * b + c * d:
                    print(f"{a}{b}{c}{d}", end=" ")
                    counter += 1
                    if counter == 4:
                        password = f"Password: {a}{b}{c}{d}"
print()
print(password)
