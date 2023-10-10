season = input()
kilometers_per_month = float(input())

price_per_km = 0

if season == "Spring" or season == "Autumn":
    if kilometers_per_month <= 5000:
        price_per_km = 0.75
    elif 5000 < kilometers_per_month <= 10000:
        price_per_km = 0.95
    elif 10000 < kilometers_per_month <= 20000:
        price_per_km = 1.45

elif season == "Summer":
    if kilometers_per_month <= 5000:
        price_per_km = 0.90
    elif 5000 < kilometers_per_month <= 10000:
        price_per_km = 1.10
    elif 10000 < kilometers_per_month <= 20000:
        price_per_km = 1.45

elif season == "Winter":
    if kilometers_per_month <= 5000:
        price_per_km = 1.05
    elif 5000 < kilometers_per_month <= 10000:
        price_per_km = 1.25
    elif 10000 < kilometers_per_month <= 20000:
        price_per_km = 1.45

money = kilometers_per_month * price_per_km * 4
tax = money * 0.1
earned_money = money - tax

print(f"{earned_money:.2f}")