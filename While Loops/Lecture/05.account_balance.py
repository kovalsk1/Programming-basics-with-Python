data = input()

amount = 0

while data != "NoMoreMoney":
    movement = float(data)

    if movement < 0:
        print("Invalid operation!")
        break
    else:
        amount += movement
        print(f"Increase: {movement:.2f}")

    data = input()

print(f"Total: {amount:.2f}")