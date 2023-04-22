import random

def chunks(l, n):
    for i in range(0, len(l), n):
        abcs = f"{l[i:i + n]} \n"
        yield abcs
n = []
for i in range(100):
    n.append(str(i))

random.shuffle(n)

print(list(chunks(n, 25)))