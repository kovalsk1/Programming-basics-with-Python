fuel_type = input()
litres_available = int(input())

if litres_available >= 25:
    if fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas":
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print("Invalid fuel!")


elif litres_available < 25:
    if fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas":
        print(f"Fill your tank with {fuel_type.lower()}!")
    else:
        print("Invalid fuel!")
