#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

the_number = number % 10 if number > 0 else int(repr(number)[-1]) * -1

if (the_number > 5):
    print(f"Last digit of {number} is {the_number} and is greater than 5")

elif (the_number == 0):
    print(f"Last digit of {number} is {the_number} and is 0")


else:
    print(f"Last digit of {number} is {the_number}\
 and is less than 6 and not 0")
