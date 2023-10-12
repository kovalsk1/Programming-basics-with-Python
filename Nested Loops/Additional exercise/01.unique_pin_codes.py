upper_limit1 = int(input())
upper_limit2 = int(input())
upper_limit3 = int(input())

for num1 in range(1, upper_limit1 + 1):
    for num2 in range(1, upper_limit2 + 1):
        for num3 in range(1, upper_limit3 + 1):
            if num1 % 2 == 0 and num3 % 2 == 0:
                if num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7:
                    print(f"{num1} {num2} {num3}")