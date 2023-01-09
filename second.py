# binary to decimal
import os
nums = os.environ["b"]
b=input()
def btod(b):
    d = 0
    for number in b:
        d = d*2 + int(number)
    print(d)
btod(b)