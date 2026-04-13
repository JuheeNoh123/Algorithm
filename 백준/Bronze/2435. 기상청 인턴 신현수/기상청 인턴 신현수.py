import sys
input = sys.stdin.readline

from math import sqrt

n,k = map(int, input().split())

temp = list(map(int,input().split()))
L = []
for i in range(0,n-k+1):
    L.append(sum(temp[i:i+k]))
#print(L)
print(max(L))
    