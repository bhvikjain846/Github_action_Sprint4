# binary to decimal
import sys
b=int(sys.argv[2])
def btod(b):
    d = 0
    for number in b:
        d = d*2 + int(number)
    print(d)
btod(b)