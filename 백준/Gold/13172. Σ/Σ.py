import sys
from collections import deque
input = sys.stdin.readline

I = 1000000007
def rec(n, s):
    if s==1 : return n
    if s%2==0:
        return (rec((n**2)%I, s//2))%I
    else:
        return (rec((n**2)%I,s//2)*n)%I
m = int(input())
s = 0
#print(rec(2,10))
for i in range(m):
    b,a = map(int,input().split())
    s+=(a*rec(b,I-2)) %I
print(s%I)
    