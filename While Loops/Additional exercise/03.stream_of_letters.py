count_c = 0
count_o = 0
count_n = 0
current_word = ""
word = ""
flag = False

while True:
    letter = input()
    if count_c >= 1 and count_o >= 1 and count_n >= 1:
        flag = True
        count_o = 0
        count_n = 0
        count_c = 0
        word += current_word
        word += " "
        current_word = ""

    if letter == "End":
        break

    if letter == "c":
        count_c += 1
        if count_c == 1:
            continue
    elif letter == "o":
        count_o += 1
        if count_o == 1:
            continue
    elif letter == "n":
        count_n += 1
        if count_n == 1:
            continue

    if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
        current_word += letter

if flag:
    print(word, end="")