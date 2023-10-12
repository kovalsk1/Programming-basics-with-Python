upper_limit_hundreds = int(input())
upper_limit_dozens = int(input())
upper_limit_numbers = int(input())

for num1 in range(1, upper_limit_hundreds + 1):
    for num2 in range(1, upper_limit_dozens + 1):
        for num3 in range(1, upper_limit_numbers + 1):
            if num1 % 2 == 0 and num3 % 2 == 0:
                if num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7:
                    print(f"{num1} {num2} {num3}")