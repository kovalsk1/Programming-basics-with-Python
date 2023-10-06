from math import ceil

tv_series = input()
time_for_episode = int(input())
time_break = int(input())

lunch_time = time_break / 8
leisure_time = time_break / 4

time_needed = time_for_episode + lunch_time + leisure_time

diff = abs(time_needed - time_break)

if time_needed <= time_break:
    print(f"You have enough time to watch {tv_series} and left with {ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_series}, you need {ceil(diff)} more minutes.")