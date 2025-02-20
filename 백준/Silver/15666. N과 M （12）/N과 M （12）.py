import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n,m = map(int, input().split())
L=list(map(int, input().split()))
L.sort()

A=[]
for i in combinations_with_replacement(L,m):
    A.append(i)
    #print(i)
A = list(set(A))    
A.sort()
for i in A:
    for j in i:
        print(j,end=' ')
    print()
