from sys import maxsize

min_number = maxsize

data = input()
while data != "Stop":
    number = int(data)

    if number < min_number:
        min_number = number

    data = input()

print(min_number)