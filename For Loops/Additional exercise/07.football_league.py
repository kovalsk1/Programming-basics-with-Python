capacity = int(input())
count_fans = int(input())

count_a = 0
count_b = 0
count_v = 0
count_g = 0

for _ in range(1, count_fans + 1):
    sector = input()

    if sector == "A":
        count_a += 1
    elif sector == "B":
        count_b += 1
    elif sector == "V":
        count_v += 1
    elif sector == "G":
        count_g += 1

print(f"{count_a / count_fans * 100:.2f}%")
print(f"{count_b / count_fans * 100:.2f}%")
print(f"{count_v / count_fans * 100:.2f}%")
print(f"{count_g / count_fans * 100:.2f}%")
print(f"{count_fans / capacity * 100:.2f}%")
