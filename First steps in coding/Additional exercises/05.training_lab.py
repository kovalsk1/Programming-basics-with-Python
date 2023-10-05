length = float(input())
width = float(input())

places_per_row = (width * 100 - 100) // 70
rows = length * 100 // 120

total_places = places_per_row * rows - 3

print(total_places)