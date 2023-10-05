count_pages = int(input())
pages_for_an_hour = int(input())
count_days = int(input())

time_needed = count_pages / pages_for_an_hour
days_needed = time_needed / count_days

print(f"{days_needed:.0f}")