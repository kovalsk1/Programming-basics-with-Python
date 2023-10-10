n = int(input())

previous_sum = 0
counter = 0

for _ in range(1, n + 1):
    number1 = int(input())
    number2 = int(input())
    current_sum = number1 + number2
    counter += 1

    if current_sum - previous_sum != 0:
        diff = abs(current_sum - previous_sum)
    else:
        diff = 0

    previous_sum = current_sum

if counter == 1:
    print(f"Yes, value={current_sum}")
elif diff == 0:
    print(f"Yes, value={current_sum}")
else:
    print(f"No, maxdiff={diff}")