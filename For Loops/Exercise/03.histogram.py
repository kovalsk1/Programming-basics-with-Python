n = int(input())

p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0
total_count = 0

for _ in range(1, n + 1):
    number = int(input())

    if number < 200:
        p1_count += 1
        total_count += 1
    elif 200 <= number <= 399:
        p2_count += 1
        total_count += 1
    elif 400 <= number <= 599:
        p3_count += 1
        total_count += 1
    elif 600 <= number <= 799:
        p4_count += 1
        total_count += 1
    elif number >= 800:
        p5_count += 1
        total_count += 1

p1_perc = p1_count / total_count * 100
p2_perc = p2_count / total_count * 100
p3_perc = p3_count / total_count * 100
p4_perc = p4_count / total_count * 100
p5_perc = p5_count / total_count * 100

print(f"{p1_perc:.2f}%")
print(f"{p2_perc:.2f}%")
print(f"{p3_perc:.2f}%")
print(f"{p4_perc:.2f}%")
print(f"{p5_perc:.2f}%")