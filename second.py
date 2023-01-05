#binary to decimal
b=1010111
def btod(b):
    d = 0
    for number in b:
        d = d*2 + int(number)
    print(d)
btod(b)