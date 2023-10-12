M = int(input())

counter = 0
flag = False
password = ""

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a*b + c*d == M:
                    if a < b and c > d:
                        counter += 1
                        print(f"{a}{b}{c}{d}", end=" ")
                        if counter == 4:
                            flag = True
                            password = f"{a}{b}{c}{d}"
                            break

if flag:
    print(f"\nPassword: {password}")
if counter < 4:
    print(f"\nNo!")
