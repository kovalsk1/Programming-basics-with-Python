length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume = length * width * height / 1000

water_needed = volume - volume * percentage / 100

print(water_needed)
