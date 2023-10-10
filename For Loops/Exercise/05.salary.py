tabs_open = int(input())
salary = float(input())

flag = False

for _ in range(1, tabs_open + 1):
    site = input()

    if site == "Facebook":
        salary -= 150
    elif site == "Instagram":
        salary -= 100
    elif site == "Reddit":
        salary -= 50

    if salary <= 0:
        flag = True
        break

if flag:
    print(f"You have lost your salary.")
else:
    print(int(salary))