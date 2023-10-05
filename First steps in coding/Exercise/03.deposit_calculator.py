deposit_amount = float(input())
term_months = int(input())
annual_interest_rate = float(input())

total_sum = deposit_amount + term_months * (deposit_amount * annual_interest_rate / 100 / 12)

print(total_sum)