count_packages_pens = int(input())
count_packages_markers = int(input())
ltr_detergent = int(input())
discount_percentage = int(input())

pens_price = count_packages_pens * 5.80
markers_price = count_packages_markers * 7.20
detergent_price = ltr_detergent * 1.20
cost = pens_price + markers_price + detergent_price

discount = cost * discount_percentage / 100

final_cost = cost - discount

print(final_cost)