count_1lv = int(input())
count_2lv = int(input())
count_5lv = int(input())
amount = int(input())

for one_lv in range(count_1lv + 1):
    for two_lv in range(count_2lv + 1):
        for five_lv in range(count_5lv + 1):
            if one_lv + two_lv * 2 + five_lv * 5 == amount:
                print(f"{one_lv} * 1 lv. + {two_lv} * 2 lv. + {five_lv} * 5 lv. = {amount} lv.")