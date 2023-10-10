student = input()

success_count = 1
failed_count = 0
total_grade = 0
flag = False

while True:
    grade = float(input())

    if grade >= 4:
        success_count += 1
        failed_count = 0
        total_grade += grade
    elif grade < 4:
        failed_count += 1

    if failed_count == 2:
        flag = True
        break
    if success_count == 13:
        break

average_grade = total_grade / 12
if flag:
    print(f"{student} has been excluded at {success_count} grade")
else:
    print(f"{student} graduated. Average grade: {average_grade:.2f}")

