V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())
P1_v = P1 * H
P2_v = P2 * H
water_v = P1_v + P2_v
if V >= water_v:
    print(
        f'The pool is {(water_v / V * 100):.2f}% full. Pipe 1: {(P1_v / water_v * 100):.2f}%. Pipe 2: {(P2_v / water_v * 100):.2f}%.')
else:
    print(f'For {H} hours the pool overflows with {(water_v - V):.2f} liters.')
