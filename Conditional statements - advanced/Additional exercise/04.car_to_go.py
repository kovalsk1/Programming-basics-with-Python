budget = float(input())
season = input()

car_class = ""
car_type = ""
price_car = 0

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        price_car = budget * 0.35
    elif season == "Winter":
        car_type = "Jeep"
        price_car = budget * 0.65

elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        price_car = budget * 0.45
    elif season == "Winter":
        car_type = "Jeep"
        price_car = budget * 0.80

elif budget > 500:
    car_class = "Luxury class"
    car_type = "Jeep"
    price_car = budget * 0.9

print(f"{car_class}")
print(f"{car_type} - {price_car:.2f}")
