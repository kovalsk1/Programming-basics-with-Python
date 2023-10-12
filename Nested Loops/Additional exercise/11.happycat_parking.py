count_days = int(input())
count_hours = int(input())

price = 0
counter_day = 0
total_sum = 0

for day in range(1, count_days + 1):
    counter_day += 1
    day_price = 0
    for hour in range(1, count_hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price = 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            price = 1.25
        else:
            price = 1
        day_price += price
        total_sum += price
    print(f"Day: {counter_day} - {day_price:.2f} leva")

print(f"Total: {total_sum:.2f} leva")