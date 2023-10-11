n = int(input())

sum_number = 0

for number in range(1, n + 1):
    number = int(input())
    sum_number += number

average = sum_number / n
print(f"{average:.2f}")