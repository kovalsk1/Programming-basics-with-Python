annual_fee = int(input())

sneakers = annual_fee * 0.6
outfit = sneakers * 0.8
ball = outfit * 0.25
accessories = ball * 0.2

total_cost = annual_fee + sneakers + outfit + ball + accessories

print(f"{total_cost}")