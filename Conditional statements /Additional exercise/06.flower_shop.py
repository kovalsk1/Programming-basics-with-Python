from math import floor, ceil

count_magnolias = int(input())
count_hyacinths = int(input())
count_roses = int(input())
count_cactuses = int(input())
gift_price = float(input())

price_magnolias = count_magnolias * 3.25
price_hyacinths = count_hyacinths * 4
price_roses = count_roses * 3.50
price_cactuses = count_cactuses * 8

revenue = price_magnolias + price_hyacinths + price_roses + price_cactuses
tax = revenue * 0.05

profit = revenue - tax

diff = abs(profit - gift_price)

if profit >= gift_price:
    print(f"She is left with {floor((diff))} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")