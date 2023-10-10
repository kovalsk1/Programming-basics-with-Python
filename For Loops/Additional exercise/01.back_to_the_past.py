inherited_money = float(input())
year_to_live = int(input())

counter = 0

for i in range(1800, year_to_live + 1):
    if i % 2 == 0:
        inherited_money -= 12000
    elif i % 2 != 0:
        inherited_money -= 12000 + (18 + counter) * 50
    counter += 1

if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")
else:
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")