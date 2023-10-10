from sys import maxsize

data = input()

max_number = -maxsize

while data != "Stop":
    number = int(data)

    if number > max_number:
        max_number = number

    data = input()

print(max_number)