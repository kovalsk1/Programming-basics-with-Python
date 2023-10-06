count_days_off = int(input())

play_during_days_off = count_days_off * 127
play_during_working_days = (365 - count_days_off) * 63

play_time = play_during_days_off + play_during_working_days

diff = abs(play_time - 30000)

hours = diff // 60
minutes = diff % 60

if play_time >= 30000:
    print(f"Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")

else:
    print(f"Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")