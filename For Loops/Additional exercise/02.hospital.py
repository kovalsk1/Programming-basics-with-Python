period = int(input())

count_treated = 0
count_untreated = 0
doctors = 7

for day in range(1, period + 1):
    if day % 3 == 0 and count_untreated > count_treated:
        doctors += 1
    patients = int(input())
    if patients <= doctors:
        count_treated += patients
    elif patients > doctors:
        count_treated += doctors
        count_untreated += patients - doctors

print(f"Treated patients: {count_treated}.")
print(f"Untreated patients: {count_untreated}.")