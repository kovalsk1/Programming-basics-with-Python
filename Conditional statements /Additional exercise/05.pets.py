from math import floor, ceil

count_days = int(input())
left_food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

food_needed = (dog_food_per_day + cat_food_per_day + turtle_food_per_day / 1000) * count_days

diff = abs(food_needed - left_food)

if food_needed <= left_food:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")