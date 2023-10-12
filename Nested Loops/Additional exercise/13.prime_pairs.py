start_value_first_couple = int(input())
start_value_second_couple = int(input())
diff_first_couple = int(input())
diff_second_couple = int(input())

for first_couple in range(start_value_first_couple, start_value_first_couple + diff_first_couple + 1):
    for second_couple in range(start_value_second_couple, start_value_second_couple + diff_second_couple + 1):
        if first_couple % 2 != 0 and first_couple % 3 != 0 and first_couple % 5 != 0 and first_couple % 7 != 0:
            if second_couple % 2 != 0 and second_couple % 3 != 0 and second_couple % 5 != 0 and second_couple % 7 != 0:
                print(f"{first_couple}{second_couple}")