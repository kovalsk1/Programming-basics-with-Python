from math import ceil, floor

sq_meters = int(input())
grapes_for_1_sq_meter = float(input())
litres_wine_needed = int(input())
count_workers = int(input())

wine_produced = sq_meters * 0.4 * grapes_for_1_sq_meter / 2.5
diff = abs(wine_produced - litres_wine_needed)

wine_per_worker = ceil(diff / count_workers)

if wine_produced < litres_wine_needed:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(wine_produced)} liters.")
    print(f"{ceil(diff)} liters left -> {wine_per_worker} liters per person.")
