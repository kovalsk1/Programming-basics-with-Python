number = int(input())

sum_numbers = 0

while True:
    current_number = int(input())
    sum_numbers += current_number

    if sum_numbers >= number:
        print(sum_numbers)
        break