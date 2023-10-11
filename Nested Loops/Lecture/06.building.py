count_floors = int(input())
count_rooms = int(input())


for floor in range(count_floors, 0, -1):
    if floor % 2 == 0:
        room_type = "O"
    else:
        room_type = "A"
    if floor == count_floors:
        room_type = "L"

    for rooms in range(0, count_rooms):
        room_name = f"{room_type}{floor}{rooms}"
        print(room_name, end=" ")

    print()