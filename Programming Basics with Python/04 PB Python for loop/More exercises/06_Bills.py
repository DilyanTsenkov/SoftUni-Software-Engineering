mounts = int(input())
water = 20 * mounts
internet = 15 * mounts
total_electricity = 0
total_other_costs = 0
for cost in range(mounts):
    electricity = float(input())
    total_electricity += electricity
    other_costs = (20 + 15 + electricity) * 1.2
    total_other_costs += other_costs
average = (water + internet + total_electricity + total_other_costs) / mounts
print(f'Electricity: {total_electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {total_other_costs:.2f} lv')
print(f'Average: {average:.2f} lv')
