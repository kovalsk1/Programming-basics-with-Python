width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height
total_boxes = 0
flag = False

data = input()

while data != "Done":
    boxes = int(data)
    total_boxes += boxes

    if total_boxes >= free_space:
        flag = True
        break

    data = input()

diff = abs(total_boxes - free_space)

if data == "Done":
    print(f"{diff} Cubic meters left.")
else:
    print(f"No more free space! You need {diff} Cubic meters more.")