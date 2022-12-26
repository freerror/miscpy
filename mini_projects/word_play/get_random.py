import random

for n in range(0, 20):
    with open("results.txt", "r") as f:
        randi = random.randint(0, 1000)
        for i, line in enumerate(f):
            if i == randi:
                print(line)
                break
    pass
