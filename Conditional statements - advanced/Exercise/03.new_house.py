type_flower = input()
count_flowers = int(input())
budget = int(input())

price = 0

if type_flower == "Roses":
    price = 5
elif type_flower == "Dahlias":
    price = 3.80
elif type_flower == "Tulips":
    price = 2.80
elif type_flower == "Narcissus":
    price = 3
elif type_flower == "Gladiolus":
    price = 2.50

total_price = price * count_flowers

if type_flower == "Roses" and count_flowers > 80:
    total_price *= 0.9
if type_flower == "Dahlias" and count_flowers > 90:
    total_price *= 0.85
if type_flower == "Tulips" and count_flowers > 80:
    total_price *= 0.85
if type_flower == "Narcissus" and count_flowers < 120:
    total_price *= 1.15
if type_flower == "Gladiolus" and count_flowers < 80:
    total_price *= 1.20

diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {count_flowers} {type_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
