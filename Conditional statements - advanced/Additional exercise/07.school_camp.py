season = input()
group_type = input()
count_students = int(input())
count_nights = int(input())

price = 0
sport = ""

if season == "Winter":
    if group_type == "girls":
        price = 9.60
        sport = "Gymnastics"
    elif group_type == "boys":
        price = 9.60
        sport = "Judo"
    elif group_type == "mixed":
        price = 10
        sport = "Ski"

elif season == "Spring":
    if group_type == "girls":
        price = 7.20
        sport = "Athletics"
    elif group_type == "boys":
        price = 7.20
        sport = "Tennis"
    elif group_type == "mixed":
        price = 9.50
        sport = "Cycling"

elif season == "Summer":
    if group_type == "girls":
        price = 15
        sport = "Volleyball"
    elif group_type == "boys":
        price = 15
        sport = "Football"
    elif group_type == "mixed":
        price = 20
        sport = "Swimming"

total_price = price * count_students * count_nights

if count_students >= 50:
    total_price *= 0.5
elif 20 <= count_students < 50:
    total_price *= 0.85
elif 10 <= count_students < 20:
    total_price *= 0.95

print(f"{sport} {total_price:.2f} lv.")