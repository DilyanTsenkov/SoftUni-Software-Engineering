last_sector = input()
first_sector_rows = int(input())
odd_places = int(input())
counter = 0
for sector in range(ord("A"), ord(last_sector) + 1):
    for row in range(1, first_sector_rows + 1):
        if row % 2 == 0:
            odd_places += 2
        for place in range(ord("a"), (97 + odd_places)):
            counter += 1
            print(f"{chr(sector)}{row}{chr(place)}")
        if row % 2 == 0:
            odd_places -= 2
    first_sector_rows += 1
print(counter)