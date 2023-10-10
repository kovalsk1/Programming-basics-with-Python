count_groups = int(input())

count_musala = 0
count_monblan = 0
count_kilimanjaro = 0
count_k2 = 0
count_everest = 0
total_count = 0

for _ in range(1, count_groups + 1):
    number_people = int(input())
    total_count += number_people
    if number_people <= 5:
        count_musala += number_people
    elif 6 <= number_people <= 12:
        count_monblan += number_people
    elif 13 <= number_people <= 25:
        count_kilimanjaro += number_people
    elif 26 <= number_people <= 40:
        count_k2 += number_people
    elif number_people >= 41:
        count_everest += number_people

perc_musala = count_musala / total_count * 100
perc_monblan = count_monblan / total_count * 100
perc_kilimanjaro = count_kilimanjaro / total_count * 100
perc_k2 = count_k2 / total_count * 100
perc_everest = count_everest / total_count * 100

print(f"{perc_musala:.2f}%")
print(f"{perc_monblan:.2f}%")
print(f"{perc_kilimanjaro:.2f}%")
print(f"{perc_k2:.2f}%")
print(f"{perc_everest:.2f}%")
