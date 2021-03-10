import random

def randInt(min= 0, max=100):
    if min > max:
        temp = min
        min = max
        max = temp
    max = max - min
    num = random.random() * max + min
    return round(num)

print(randInt(10, 50))