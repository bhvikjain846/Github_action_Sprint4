# decimal to binary
import os
nums = os.environ["d"]
d=input(nums)
def dtob(d):
    if d > 1:
        dtob(d // 2)
    print(d%2,end='')
dtob(int(d))
