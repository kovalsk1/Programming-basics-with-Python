data = input()

while data != "End":
    savings = 0
    destination = data
    budget = (float(input()))
    while savings < budget:
        save_amount = float(input())
        savings += save_amount

        if savings >= budget:
            print(f"Going to {destination}!")
            break

    data = input()