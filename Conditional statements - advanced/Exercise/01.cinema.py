projection_type = input()
count_rows = int(input())
count_columns = int(input())

number_tickets = count_rows * count_columns
ticket_price = 0


if projection_type == "Premiere":
    ticket_price = 12
elif projection_type == "Normal":
    ticket_price = 7.50
elif projection_type == "Discount":
    ticket_price = 5

total_price = number_tickets * ticket_price

print(f"{total_price:.2f}")