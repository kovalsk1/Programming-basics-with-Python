hours = int(input())
minutes = int(input())

total_minutes =  hours * 60 + minutes
after_15_minutes = total_minutes + 15

new_hours = after_15_minutes // 60
new_minutes = after_15_minutes % 60

if new_hours == 24:
    new_hours = 0

print(f"{new_hours}:{new_minutes:02}")
