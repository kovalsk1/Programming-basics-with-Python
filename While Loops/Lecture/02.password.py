user = input()
password = input()

while True:
    input_pass = input()

    if input_pass == password:
        print(f"Welcome {user}!")
        break