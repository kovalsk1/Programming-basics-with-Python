a = int(input())
b = int(input())
max_passwords = int(input())

counter = 0
flag = False

for A in range(35, 56):
    for B in range(64, 97):
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
                counter += 1

                A += 1
                if A == 56:
                    A = 35
                B += 1
                if B == 97:
                    B = 64

                if counter == max_passwords:
                    flag = True
                    break
            if flag:
                break
        break
    break