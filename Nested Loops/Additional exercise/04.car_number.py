start_interval = int(input())
end_interval = int(input())

for num1 in range(start_interval, end_interval + 1):
    for num2 in range(start_interval, end_interval + 1):
        for num3 in range(start_interval, end_interval + 1):
            for num4 in range(start_interval, end_interval + 1):
                if num1 % 2 == 0 and num4 % 2 != 0:
                    if num1 > num4:
                        if (num2 + num3) % 2 == 0:
                            print(f"{num1}{num2}{num3}{num4}", end=" ")
                elif num1 % 2 != 0 and num4 % 2 == 0:
                    if num1 > num4:
                        if (num2 + num3) % 2 == 0:
                            print(f"{num1}{num2}{num3}{num4}", end=" ")