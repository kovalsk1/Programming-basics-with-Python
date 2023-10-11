count_jury = int(input())
data = input()

total_assesment = 0
counter = 0

while data != "Finish":
    presentation = data
    presentation_assessment = 0
    for _ in range(1, count_jury + 1):
        assessment = float(input())
        presentation_assessment += assessment
        total_assesment += assessment
        counter += 1

    average_presentation = presentation_assessment / count_jury
    print(f"{presentation} - {average_presentation:.2f}.")

    data = input()

average_total = total_assesment / counter

print(f"Student's final assessment is {average_total:.2f}.")