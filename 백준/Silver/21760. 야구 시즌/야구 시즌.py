import sys
from itertools import combinations
input=sys.stdin.readline

n = int(input())
for _ in range(n):
    N,M,K,D = map(int, input().split())
    local = (M*(M-1)//2)*N*K
    other = (N*(N-1)//2)*(M**2)
    total=D//(local + other)
    if(total!=0):
        print((local + other)*total)
    else:
        print(-1)
