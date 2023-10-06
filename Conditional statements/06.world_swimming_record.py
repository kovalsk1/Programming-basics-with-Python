from math import floor

current_record = float(input())
distance = float(input())
time_for_1_meter = float(input())

resistance = floor(distance / 15)
additional_time = resistance * 12.50

time = distance * time_for_1_meter + additional_time

diff = abs(time - current_record)

if time < current_record:
    print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")