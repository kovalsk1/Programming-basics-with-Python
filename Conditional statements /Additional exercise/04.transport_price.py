kilometres = int(input())
time = input()

price = 0

if kilometres < 20:
    if time == "day":
        price = 0.7 + kilometres * 0.79
    elif time == "night":
        price = 0.7 + kilometres * 0.9

elif 20 <= kilometres < 100:
    price = kilometres * 0.09

elif kilometres >= 100:
    price = kilometres * 0.06

print(f"{price:.2f}")