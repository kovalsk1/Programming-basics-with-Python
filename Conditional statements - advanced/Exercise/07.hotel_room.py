month = input()
count_nights = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77

if 7 < count_nights <= 14:
    if month == "May" or month == "October":
        studio_price *= 0.95
elif count_nights > 14:
    if month == "May" or month == "October":
        studio_price *= 0.70
    elif month == "June" or month == "September":
        studio_price *= 0.8
if count_nights > 14:
    apartment_price *= 0.9

total_price_studio = studio_price * count_nights
total_price_apartment = apartment_price * count_nights

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
