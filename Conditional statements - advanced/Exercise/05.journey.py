budget = float(input())
season = input()

type_vacation = ""
destination = ""
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_vacation = "Camp"
        price = budget * 0.3
    elif season == "winter":
        type_vacation = "Hotel"
        price = budget * 0.7

elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_vacation = "Camp"
        price = budget * 0.4
    elif season == "winter":
        type_vacation = "Hotel"
        price = budget * 0.8

elif budget > 1000:
    destination = "Europe"
    if season == "summer":
        type_vacation = "Hotel"
        price = budget * 0.9
    elif season == "winter":
        type_vacation = "Hotel"
        price = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{type_vacation} - {price:.2f}")