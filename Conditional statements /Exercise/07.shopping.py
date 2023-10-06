budget = float(input())
count_videocards = int(input())
count_processors = int(input())
count_ram_memory = int(input())

price_videocards = count_videocards * 250
price_processors = price_videocards * 0.35 * count_processors
price_ram_memory = price_videocards * 0.1 * count_ram_memory

total_price = price_videocards + price_processors + price_ram_memory

if count_videocards > count_processors:
    total_price *= 0.85

diff = abs(total_price - budget)

if total_price <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")