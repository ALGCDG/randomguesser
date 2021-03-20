from sys import stdin
import random

for line in stdin:
    if line == '':
        break
    print(random.randint(0,1))
