import time
import random
rnd_length = int(input("Enter Round Length (seconds): "))
start_time = time.time()
num_correct = 0
num_attempted = 0
while (time.time() - start_time) < rnd_length:
    x = random.randint(0, 200)
    y = random.randint(0, x)
    # no divisions for now
    op = random.choice(['+', '-', '*'])
    pred = int(input(f"{x} {op} {y}: "))
    actual = eval(f'x {op} y')
    if pred == actual:
        num_correct += 1
    num_attempted += 1

print(f"Got {num_correct} correct out of {num_attempted} questions.\n{num_correct/num_attempted} success rate.")
    