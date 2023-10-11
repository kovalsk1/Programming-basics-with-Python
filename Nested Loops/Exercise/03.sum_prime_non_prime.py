data = input()

sum_prime = 0
sum_non_prime = 0

while data != "stop":
    number = int(data)

    if number < 0:
        print("Number is negative.")
        data = input()
        continue

    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        sum_prime += number
    else:
        sum_non_prime += number

    data = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")