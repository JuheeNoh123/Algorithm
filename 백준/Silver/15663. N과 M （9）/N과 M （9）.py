import sys
from itertools import permutations
input = sys.stdin.readline


n,m = map(int, input().split())
L=list(map(int, input().split()))
A=set()
for i in permutations(L,m):
    A.add(i)
    
A = list(A)
A.sort()

for i in A:
    for j in i:
        print(j,end=' ')
    print()