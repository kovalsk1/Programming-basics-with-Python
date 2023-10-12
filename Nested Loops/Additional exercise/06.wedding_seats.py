last_sector = input()
cont_rows_first_sector = int(input())
places_odd_row = int(input())

counter = 0

for sector in range(ord("A"), ord(last_sector) + 1):
    for rows in range(1, cont_rows_first_sector + 1):
        if rows % 2 != 0:
            for places in range(ord("a"), ord("a") + places_odd_row):
                print(f"{chr(sector)}{rows}{chr(places)}")
                counter += 1
        if rows % 2 == 0:
            for places in range(ord("a"), ord("a") + places_odd_row + 2):
                print(f"{chr(sector)}{rows}{chr(places)}")
                counter += 1
    cont_rows_first_sector += 1

print(counter)