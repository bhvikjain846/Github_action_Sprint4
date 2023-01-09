# decimal to binary
import sys
d=int(sys.argv[1])
def dtob(d):
    if d > 1:
        dtob(d // 2)
    print(d%2,end='')
dtob(int(d))
