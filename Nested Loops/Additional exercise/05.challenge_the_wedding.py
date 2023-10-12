count_men = int(input())
count_women = int(input())
max_tables = int(input())

counter = 0
flag = False

for men in range(1, count_men + 1):
    for women in range(1, count_women + 1):
        counter += 1
        print(f"({men} <-> {women})", end=" ")

        if counter == max_tables:
            flag = True
            break

    if flag:
        break

