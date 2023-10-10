favourite_book = input()

flag = False
counter = 0

data = input()
while data != "No More Books":
    book = data

    if book == favourite_book:
        flag = True
        break

    counter += 1
    data = input()

if flag:
    print(f"You checked {counter} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {counter} books.")
