start_interval = input()
end_interval = input()
skip_letter = input()

counter = 0

for letter1 in range(ord(start_interval), ord(end_interval) + 1):
    for letter2 in range(ord(start_interval), ord(end_interval) + 1):
        for letter3 in range(ord(start_interval), ord(end_interval) + 1):
            if letter1 != ord(skip_letter) and letter2 != ord(skip_letter) and letter3 != ord(skip_letter):
                print(f"{chr(letter1)}{chr(letter2)}{chr(letter3)}", end=" ")
                counter += 1

print(counter)