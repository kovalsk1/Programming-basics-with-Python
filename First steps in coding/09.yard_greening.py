sq_meters = float(input())

price_sq_m = 7.61

cost = sq_meters * price_sq_m
discount = cost * 0.18
final_cost = cost - discount

print(f"The final price is: {final_cost} lv.")
print(f"{discount}")