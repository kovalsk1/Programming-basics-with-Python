vacation_price = float(input())
count_puzzles = int(input())
count_talking_dolls = int(input())
count_teddy_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

price_puzzles = count_puzzles * 2.60
price_talking_dolls = count_talking_dolls * 3
price_teddy_bears = count_teddy_bears * 4.10
price_minions = count_minions * 8.20
price_trucks = count_trucks * 2

total_price = price_puzzles + price_talking_dolls + price_teddy_bears + price_minions + price_trucks

count_all = count_puzzles + count_talking_dolls + count_teddy_bears + count_minions + count_trucks

if count_all >= 50:
    total_price *= 0.75

rent = total_price * 0.1
profit = total_price - rent
diff = abs(vacation_price - profit)

if profit >= vacation_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
