age_lily = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

saved_money = 0
counter_toys = 0

for i in range(1, age_lily + 1):
    if i % 2 == 0:
        saved_money += int(i / 2) * 10
        saved_money -= 1
    elif i % 2 != 0:
        counter_toys += 1

total_money = saved_money + counter_toys * price_per_toy
diff = abs(total_money - washing_machine_price)

if total_money >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
