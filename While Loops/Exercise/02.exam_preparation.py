negative_grade_count = int(input())

data = input()
failed_count = 0
flag = False
total_grade = 0
count = 0

while data != "Enough":
    task = data
    grade = int(input())
    total_grade += grade
    count += 1

    if grade <= 4:
        failed_count += 1

    if failed_count == negative_grade_count:
        flag = True
        break

    data = input()

average_grade = total_grade / count

if not flag:
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {count}")
    print(f"Last problem: {task}")
if flag:
    print(f"You need a break, {failed_count} poor grades.")