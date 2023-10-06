volume_pool = int(input())
debit_first_pipe_for_an_hour = int(input())
debit_second_pipe_for_an_hour = int(input())
hours = float(input())

water = (debit_first_pipe_for_an_hour + debit_second_pipe_for_an_hour) * hours

percentage_first_pipe = debit_first_pipe_for_an_hour * hours / water * 100
percentage_second_pipe = debit_second_pipe_for_an_hour * hours / water * 100
percentage_full = water / volume_pool * 100
diff = abs(volume_pool - water)

if water <= volume_pool:
    print(f"The pool is {percentage_full:.2f}% full. Pipe 1: {percentage_first_pipe:.2f}%. Pipe 2: "
          f"{percentage_second_pipe:.2f}%.")
else:
    print(f"For {hours} hours the pool overflows with {diff:.2f} liters.")

