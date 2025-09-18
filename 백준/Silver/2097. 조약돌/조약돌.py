import sys

input = sys.stdin.readline

n = int(input())
if n==1 or n==2:
    print(4)
else:
    for i in range(2,n+1):
        if n<=i*i:
            print((i-1)*4)
            break
        elif n<=i*(i+1):
            print((2*i-1)*2)
            break
        