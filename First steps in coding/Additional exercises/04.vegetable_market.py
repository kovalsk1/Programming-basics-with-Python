price_vegetables_kg = float(input())
price_fruits_kg = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())

revenue_bgn = vegetables_kg * price_vegetables_kg + fruits_kg * price_fruits_kg
revenue_eur = revenue_bgn / 1.94

print(f"{revenue_eur:.2f}")