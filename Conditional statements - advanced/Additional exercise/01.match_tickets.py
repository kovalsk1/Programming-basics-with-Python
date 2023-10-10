budget = float(input())
category = input()
count_people = int(input())

ticket_price = 0
transport_price = 0

if category == "VIP":
    ticket_price = 499.99
elif category == "Normal":
    ticket_price = 249.99

if count_people <= 4:
    transport_price = budget * 0.75
elif  5 <= count_people <= 9:
    transport_price = budget * 0.6
elif 10 <= count_people <= 24:
    transport_price = budget * 0.5
elif 25 <= count_people <= 49:
    transport_price = budget * 0.4
elif count_people >= 50:
    transport_price = budget * 0.25

total_price = ticket_price * count_people + transport_price

diff = abs(total_price - budget)

if budget >= total_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")