import time
import random
rnd_length = int(input("Enter Round Length (seconds): "))
num_correct = 0
num_attempted = 0
start_time = time.time()
while (time.time() - start_time) < rnd_length:
    op = random.choice(['+', '-', '*', '**'])
    if op == "**":
        x = random.randint(2, 100)
        if x > 20:
            x -= x % 5
        y = 2
    else:
        if op == "*":
            max_val = 60
        else:
            max_val = 500
        x = random.randint(0, max_val)
        y = random.randint(0, x)
    # no divisions for now
    # op = random.choice(['+', '-', '*'])
    pred = int(input(f"{x} {op} {y}: "))
    actual = eval(f'x {op} y')
    if pred == actual:
        num_correct += 1
        print('correct')
    else:
        print(f"answer: {actual}")
    num_attempted += 1

print(f"Got {num_correct} correct out of {num_attempted} questions.\n{num_correct/num_attempted} success rate.")
    