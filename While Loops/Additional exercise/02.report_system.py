target_amount = int(input())

counter = 0
count_card = 0
count_cash = 0
collected_money = 0
card_amount = 0
cash_amount = 0

data = input()
while data != "End":
    price = int(data)
    counter += 1

    if counter % 2 != 0:
        if price <= 100:
            count_cash += 1
            cash_amount += price
            collected_money += price
            print("Product sold!")
        else:
            print(f"Error in transaction!")
    elif counter % 2 == 0:
        if price >= 10:
            count_card += 1
            card_amount += price
            collected_money += price
            print("Product sold!")
        else:
            print(f"Error in transaction!")

    if collected_money >= target_amount:
        print(f"Average CS: {cash_amount/count_cash:.2f}")
        print(f"Average CC: {card_amount/count_card:.2f}")
        break

    data = input()
if data == "End":
    print(f"Failed to collect required money for charity.")
