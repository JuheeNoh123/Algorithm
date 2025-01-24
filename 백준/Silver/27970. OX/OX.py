import sys
input = sys.stdin.readline

a = input().strip()
#print(len(a))
b = len(a)
# L=[2**i for i in range(b)]
# print(L)
sum=0
if b==1:
    if a=='O':
        print(1)
    else:
        print(0)
else:
    for i in range(b):
        if a[i]=='O':
            sum += 2**i
        
    print(sum%(10**9+7))