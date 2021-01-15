n = int(input())


def range_start_end(r):
    result = set()
    start_number, end_number = (int(x) for x in r.split(","))
    for number in range(start_number, end_number + 1):
        result.add(number)
    return result


max_intersection = []

for _ in range(n):
    first_range, second_range = input().split("-")
    f_range = range_start_end(first_range)
    s_range = range_start_end(second_range)
    f_s_intersection = f_range.intersection(s_range)
    if len(max_intersection) < len(f_s_intersection):
        max_intersection = f_s_intersection

print(f"Longest intersection is {list(max_intersection)} with length {len(max_intersection)}")
