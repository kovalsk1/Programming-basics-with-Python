months = int(input())

total_electricity = 0
total_water = 0
total_internet = 0
total_others = 0

for _ in range(1, months + 1):
    electricity = float(input())
    total_electricity += electricity
    water = 20
    total_water += water
    internet = 15
    total_internet += internet
    other = (electricity + water + internet) * 1.2
    total_others += other

average = (total_electricity + total_water + total_others + total_internet) / months

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_others:.2f} lv")
print(f"Average: {average:.2f} lv")