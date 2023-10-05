nylon_needed_sq_m = int(input())
paint_needed_ltr = int(input())
paint_thinner_ltr = int(input())
labour_hours = int(input())

nylon_price = (nylon_needed_sq_m + 2) * 1.50
paint_price = paint_needed_ltr * 14.50 * 1.1
paint_thinner_price = paint_thinner_ltr * 5
all_materials = nylon_price + paint_price + paint_thinner_price + 0.4

labour_cost = labour_hours * all_materials * 0.3

all_cost = all_materials + labour_cost

print(f"{all_cost}")
