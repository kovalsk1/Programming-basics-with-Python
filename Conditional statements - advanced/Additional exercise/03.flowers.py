count_chrysanthemum = int(input())
count_roses = int(input())
count_tulips = int(input())
season = input()
holiday = input()

count_flowers = count_chrysanthemum + count_roses + count_tulips
price_chrysanthemum = 0
price_roses = 0
price_tulips = 0

if season == "Spring" or season == "Summer":
    price_chrysanthemum = 2
    price_roses = 4.10
    price_tulips = 2.50
elif season == "Autumn" or season == "Winter":
    price_chrysanthemum = 3.75
    price_roses = 4.50
    price_tulips = 4.15

if holiday == "Y":
    price_chrysanthemum *= 1.15
    price_roses *= 1.15
    price_tulips *= 1.15

price_flowers = count_chrysanthemum * price_chrysanthemum + count_roses * price_roses + count_tulips * price_tulips

if season == "Spring" and count_tulips > 7:
    price_flowers *= 0.95
if season == "Winter" and count_roses >= 10:
    price_flowers *= 0.9
if count_flowers > 20:
    price_flowers *= 0.8

final_price = price_flowers + 2

print(f"{final_price:.2f}")