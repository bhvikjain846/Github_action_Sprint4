#binary to decimal
b=input("Enter a binary no.: ")
def btod(b):
    d = 0
    for number in b:
        d = d*2 + int(number)
    print(d)
btod(b)