count_dish_washer = int(input())

dish_washer = count_dish_washer * 750
counter = 0
count_pots =0
count_plates = 0
flag = False

data = input()
while data != "End":
    count_dishes = int(data)
    counter += 1
    if counter % 3 == 0:
        count_pots += count_dishes
        dish_washer -= count_dishes * 15
    else:
        count_plates += count_dishes
        dish_washer -= count_dishes * 5

    if dish_washer < 0:
        flag = True
        break

    data = input()

if dish_washer >= 0:
    print("Detergent was enough!")
    print(f"{count_plates} dishes and {count_pots} pots were washed.")
    print(f"Leftover detergent {dish_washer} ml.")
else:
    print(f"Not enough detergent, {abs(dish_washer)} ml. more necessary!")
