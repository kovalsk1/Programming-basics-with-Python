n1 = int(input())
n2 = int(input())
operator = input()

result = 0
flag = False

if operator == "+":
    result = n1 + n2
elif operator == "-":
    result = n1 - n2
elif operator == "*":
    result = n1 * n2

elif operator == "/":
    if n2 == 0:
        flag = True
    else:
        result = n1 / n2


elif operator == "%":
    if n2 == 0:
        flag = True
    else:
        result = n1 % n2

if operator == "+" or operator == "-" or operator == "*":
    if result % 2 == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")

if operator == "/":
    if flag:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} / {n2} = {result:.2f}")

if operator == "%":
    if flag:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} % {n2} = {result}")
