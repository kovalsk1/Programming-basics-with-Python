length = int(input())
width = int(input())

cake_pieces = length * width
flag = False
data = input()

while data != "STOP":
    pieces = int(data)
    cake_pieces -= pieces

    if cake_pieces <= 0:
        flag = True
        break

    data = input()

diff = abs(cake_pieces)

if flag:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{diff} pieces are left.")