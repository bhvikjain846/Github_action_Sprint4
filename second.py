print("My name is Bhvik Jain")

# binary to decimal
b=input()
def btod(b):
    d = 0
    for number in b:
        d = d*2 + int(number)
    print(d)
btod(b)