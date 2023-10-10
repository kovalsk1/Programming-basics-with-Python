from math import floor

count_tournamets = int(input())
starting_points = int(input())

points = 0
counter_wins = 0

for _ in range(1, count_tournamets + 1):
    stage = input()

    if stage == "W":
        points += 2000
        counter_wins += 1
    elif stage == "F":
        points += 1200
    elif stage == "SF":
        points += 720

all_points = starting_points + points
average_points = points / count_tournamets
perc_wins = counter_wins / count_tournamets * 100

print(f"Final points: {all_points}")
print(f"Average points: {floor(average_points)}")
print(f"{perc_wins:.2f}%")

