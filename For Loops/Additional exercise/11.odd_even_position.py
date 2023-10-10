n = int(input())

odd_min = 100
odd_max = -100
even_min = 100
even_max = -100
odd_sum = 0
even_sum = 0
counter_even = 0
counter_odd = 0


for i in range(1, n + 1):
    number = float(input())

    if i % 2 != 0:
        counter_odd += 1
        odd_sum += number
        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number
    elif i % 2 == 0:
        counter_even += 1
        even_sum += number
        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number

print(f"OddSum={odd_sum:.2f},")
if counter_odd < 1:
    print(f"No")
else:
    print(f"OddMin={odd_min:.2f},")
if counter_odd < 1:
    print(f"No,")
else:
    print(f"OddMax={odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
if counter_even < 1:
    print(f"No,")
else:
    print(f"EvenMin={even_min:.2f},")
if counter_even < 1:
    print(f"No")
else:
    print(f"EvenMax={even_max:.2f}")