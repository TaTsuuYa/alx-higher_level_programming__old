#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is", end="")
if (number < 0):
    mod = -number % 10
    print(f" -{mod}", end="")
else:
    mod = number % 10
    print(f" {mod}", end="")

if (number > 0 and mod > 5):
    print(" and is greater than 5")
if (mod == 0):
    print(" and is 0")
if (number < 0 or (mod < 6 and mod != 0)):
    print(" and is less than 6 and not 0")
