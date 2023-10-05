count_chicken_menus = int(input())
count_fish_menus = int(input())
count_veggie_menus = int(input())

chicken_price = count_chicken_menus * 10.35
fish_price = count_fish_menus * 12.40
veggie_price = count_veggie_menus * 8.15

cost = chicken_price + fish_price + veggie_price
desert = cost * 0.2

total_cost = cost + desert + 2.50

print(f"{total_cost}")