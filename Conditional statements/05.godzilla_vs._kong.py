budget = float(input())
count_statists = int(input())
price_clothes_per_statist = float(input())

price_decor = budget * 0.1

price_clothes = count_statists * price_clothes_per_statist

if count_statists > 150:
    price_clothes *= 0.9

all_cost = price_decor + price_clothes
diff = abs(all_cost - budget)

if all_cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")