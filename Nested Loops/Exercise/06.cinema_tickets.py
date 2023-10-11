data = input()
total_counter = 0
student_counter = 0
standard_counter = 0
kid_counter = 0

while data != "Finish":
    movie = data
    capacity = int(input())
    input_line = input()
    counter_movie = 0
    while input_line != "End":
        ticket_type = input_line
        counter_movie += 1
        total_counter += 1

        if ticket_type == "student":
            student_counter += 1
        elif ticket_type == "standard":
            standard_counter += 1
        elif ticket_type == "kid":
            kid_counter += 1

        if counter_movie == capacity:
            break

        input_line = input()

    perc_full = counter_movie / capacity * 100
    print(f"{movie} - {perc_full:.2f}% full.")

    data = input()

print(f"Total tickets: {total_counter}")
print(f"{student_counter / total_counter * 100:.2f}% student tickets.")
print(f"{standard_counter / total_counter * 100:.2f}% standard tickets.")
print(f"{kid_counter / total_counter * 100:.2f}% kids tickets.")