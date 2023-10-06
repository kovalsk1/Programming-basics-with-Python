participant1 = int(input())
participant2 = int(input())
participant3 = int(input())

sum_seconds = participant1 + participant2 + participant3
# 124 seconds

minutes = sum_seconds // 60
seconds = sum_seconds % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
