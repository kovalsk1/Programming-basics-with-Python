starting_bonus_points = int(input())

additional_points = 0

if starting_bonus_points <= 100:
    additional_points = 5
elif 100 < starting_bonus_points <= 1000:
    additional_points = starting_bonus_points * 0.2
elif starting_bonus_points > 1000:
    additional_points = starting_bonus_points * 0.1

if starting_bonus_points % 2 == 0:
    additional_points += 1

if starting_bonus_points % 10 == 5:
    additional_points += 2

total_points = starting_bonus_points + additional_points

print(additional_points)
print(total_points)