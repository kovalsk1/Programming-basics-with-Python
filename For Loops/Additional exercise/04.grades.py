count_students = int(input())

top_students = 0
between_4_and_5 = 0
between_3_and_4 = 0
fail = 0
total_grade = 0

for _ in range(1, count_students + 1):
    grade = float(input())
    total_grade += grade
    if grade < 3:
        fail += 1
    elif 3 <= grade <= 3.99:
        between_3_and_4 += 1
    elif 4 <= grade <= 4.99:
        between_4_and_5 += 1
    elif grade >= 5:
        top_students += 1

average = total_grade / count_students
perc_top_students = top_students / count_students * 100
perc_between_4_and_5 = between_4_and_5 / count_students * 100
perc_between_3_and_4 = between_3_and_4 / count_students * 100
perc_fail = fail / count_students * 100

print(f"Top students: {perc_top_students:.2f}%")
print(f"Between 4.00 and 4.99: {perc_between_4_and_5:.2f}%")
print(f"Between 3.00 and 3.99: {perc_between_3_and_4:.2f}%")
print(f"Fail: {perc_fail:.2f}%")
print(f"Average: {average:.2f}")