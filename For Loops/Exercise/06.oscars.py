actor = input()
academy_points = float(input())
count_jury = int(input())

flag = False
points = 0

for _ in range(1, count_jury + 1):
    jury = input()
    jury_points = float(input())
    points += len(jury) * jury_points / 2

    if academy_points + points > 1250.5:
        flag = True
        break

all_points = academy_points + points

if flag:
    print(f"Congratulations, {actor} got a nominee for leading role with {all_points:.1f}!")
else:
    diff = abs(1250.5 - all_points)
    print(f"Sorry, {actor} you need {diff:.1f} more!")


