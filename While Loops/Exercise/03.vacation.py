money_needed = float(input())
available_money = float(input())

spend_counter = 0
counter = 0
flag = False

while True:
    if spend_counter == 5:
        flag = True
        break
    action = input()
    amount = float(input())
    counter += 1

    if action == "spend":
        spend_counter += 1
        available_money -= amount
        if available_money < 0:
            available_money = 0
    elif action == "save":
        available_money += amount
        spend_counter = 0

    if available_money >= money_needed:
        break

if flag:
    print(f"You can't save the money.")
    print(f"{counter}")
else:
    print(f"You saved the money for {counter} days.")

