exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes

diff = abs(exam_time - arrival_time)

if arrival_time > exam_time:
    print("Late")
    if diff >= 60:
        diff_hour = diff // 60
        diff_minutes = diff % 60
        print(f"{diff_hour}:{diff_minutes:02} hours after the start")
    elif diff < 60:
        print(f"{diff} minutes after the start")

elif arrival_time < exam_time and diff > 30:
    print("Early")
    if diff >= 60:
        diff_hour = diff // 60
        diff_minutes = diff % 60
        print(f"{diff_hour}:{diff_minutes:02} hours before the start")
    elif diff < 60:
        print(f"{diff} minutes before the start")

else:
    print("On time")
    if diff != 0:
        print(f"{diff} minutes before the start")
