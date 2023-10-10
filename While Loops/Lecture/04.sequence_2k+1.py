n = int(input())

current_number = 0

while True:
    current_number = current_number * 2 + 1

    if current_number > n:
        break

    print(current_number)