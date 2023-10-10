moves = int(input())

points = 0
counter_0_to_9 = 0
counter_10_to_19 = 0
counter_20_to_29 = 0
counter_30_to_39 = 0
counter_40_to_50 = 0
invalid_counter = 0

for _ in range(1, moves + 1):
    number = int(input())

    if 0 <= number <= 9:
        points += number * 0.2
        counter_0_to_9 += 1
    elif 10 <= number <= 19:
        points += number * 0.3
        counter_10_to_19 += 1
    elif 20 <= number <= 29:
        points += number * 0.4
        counter_20_to_29 += 1
    elif 30 <= number <= 39:
        points += 50
        counter_30_to_39 += 1
    elif 40 <= number <= 50:
        points += 100
        counter_40_to_50 += 1
    elif number < 0 or number > 50:
        points /= 2
        invalid_counter += 1

print(f"{points:.2f}")
print(f"From 0 to 9: {counter_0_to_9 / moves * 100:.2f}%")
print(f"From 10 to 19: {counter_10_to_19 / moves * 100:.2f}%")
print(f"From 20 to 29: {counter_20_to_29 / moves * 100:.2f}%")
print(f"From 30 to 39: {counter_30_to_39 / moves * 100:.2f}%")
print(f"From 40 to 50: {counter_40_to_50 / moves * 100:.2f}%")
print(f"Invalid numbers: {invalid_counter / moves * 100:.2f}%")