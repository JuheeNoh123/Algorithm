import sys
input = sys.stdin.readline

from math import sqrt

a = input()
cnt0=0
cnt1=0
for i in a:
    if i=='0':
        cnt0+=1
    else:
        cnt1+=1
n_0 = '0' * (cnt0//2)
n_1 = '1' * (cnt1//2)

print(n_0+n_1)