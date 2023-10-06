fuel_type = input()
quantity_fuel = float(input())
club_card = input()

price = 0

if fuel_type == "Gasoline":
    price = 2.22
    if club_card == "Yes":
        price -= 0.18
elif fuel_type == "Diesel":
    price = 2.33
    if club_card == "Yes":
        price -= 0.12
elif fuel_type == "Gas":
    price = 0.93
    if club_card == "Yes":
        price -= 0.08

total_price = price * quantity_fuel

if 20 <= quantity_fuel <= 25:
    total_price *= 0.92
elif quantity_fuel > 25:
    total_price *= 0.90

print(f"{total_price:.2f} lv.")