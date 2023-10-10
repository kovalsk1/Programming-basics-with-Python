data = input()

total_steps = 0
flag = False

while data != "Going home":
    steps = int(data)
    total_steps += steps

    if total_steps >= 10000:
        flag = True
        break

    data = input()

if data == "Going home":
    steps_home = int(input())
    total_steps += steps_home

diff = abs(total_steps - 10000)

if total_steps >= 10000:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")