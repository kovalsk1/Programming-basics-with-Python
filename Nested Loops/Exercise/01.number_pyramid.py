n = int(input())

flag = False
counter = 0

for row in range(1, n + 1):
    for column in range(1, row + 1):
        counter += 1
        if counter > n:
            flag = True
            break
        print(str(counter) + " ", end="")

    if flag:
        break
    print()