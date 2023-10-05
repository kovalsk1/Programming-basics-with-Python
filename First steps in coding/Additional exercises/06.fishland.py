price_mackerel = float(input())
price_sprinkle = float(input())
bonito_kg = float(input())
safrid_kg = float(input())
mussels_kg = float(input())

bonito_cost = bonito_kg * price_mackerel * 1.6
safrid_cost = safrid_kg * price_sprinkle * 1.8
mussels_cost = mussels_kg * 7.50

all_cost = bonito_cost + safrid_cost + mussels_cost

print(f"{all_cost:.2f}")