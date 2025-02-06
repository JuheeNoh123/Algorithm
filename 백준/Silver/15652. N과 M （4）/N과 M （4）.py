import sys
from collections import deque
import itertools
input = sys.stdin.readline

N,M = map(int, input().split())

L=[i for i in range(1,N+1)]


for i in itertools.combinations_with_replacement(L,M):
   for j in i:
      print(j, end=' ')
   print()