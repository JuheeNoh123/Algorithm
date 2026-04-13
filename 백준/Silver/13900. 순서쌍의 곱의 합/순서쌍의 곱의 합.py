import sys
input = sys.stdin.readline

from math import sqrt

n=int(input())

L = list(map(int,input().split()))
d=[L[i] for i in range(n)]

for i in range(n-2,-1,-1):
    d[i] += d[i+1]
sum=0
for i in range(n-1):
    sum += L[i]*d[i+1]
print(sum)