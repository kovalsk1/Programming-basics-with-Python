count_cargo = int(input())

bus_count = 0
truck_count = 0
train_count = 0
tons_count = 0
price = 0
total_price = 0

for _ in range(1, count_cargo + 1):
    cargo_weight = int(input())
    tons_count += cargo_weight

    if cargo_weight <= 3:
        price = 200 * cargo_weight
        bus_count += cargo_weight
    elif 4 <= cargo_weight <= 11:
        price = 175 * cargo_weight
        truck_count += cargo_weight
    elif cargo_weight >= 12:
        price = 120 * cargo_weight
        train_count += cargo_weight
    total_price += price

average_price = total_price / tons_count
perc_bus = bus_count / tons_count * 100
perc_truck = truck_count / tons_count * 100
perc_train = train_count / tons_count * 100

print(f"{average_price:.2f}")
print(f"{perc_bus:.2f}%")
print(f"{perc_truck:.2f}%")
print(f"{perc_train:.2f}%")