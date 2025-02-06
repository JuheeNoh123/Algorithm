import sys
from collections import deque
import itertools
input = sys.stdin.readline

N,M = map(int, input().split())

L=[i for i in range(1,N+1)]
nCr = list(itertools.combinations(L,M))

for i in nCr:
   for j in i:
      print(j, end=' ')
   print()