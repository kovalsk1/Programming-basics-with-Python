count_juniors = int(input())
count_seniors = int(input())
track = input()

price_juniors = 0
price_seniors = 0

if track == "trail":
    price_juniors = 5.50
    price_seniors = 7
elif track == "cross-country":
    price_juniors = 8
    price_seniors = 9.50
    if count_juniors + count_seniors >= 50:
        price_juniors *= 0.75
        price_seniors *= 0.75
elif track == "downhill":
    price_juniors = 12.25
    price_seniors = 13.75
elif track == "road":
    price_juniors = 20
    price_seniors = 21.50

total_price = count_juniors * price_juniors + count_seniors * price_seniors
cost = total_price * 0.05

final_price = total_price - cost

print(f"{final_price:.2f}")