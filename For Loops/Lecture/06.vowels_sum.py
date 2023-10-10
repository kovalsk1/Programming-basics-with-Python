word = input()

points = 0

for i in range(len(word)):
    if word[i] == "a":
        points += 1
    if word[i] == "e":
        points += 2
    if word[i] == "i":
        points += 3
    if word[i] == "o":
        points += 4
    if word[i] == "u":
        points += 5

print(points)