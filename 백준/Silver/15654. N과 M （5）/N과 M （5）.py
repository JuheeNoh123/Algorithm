import sys
from collections import deque
import itertools
input = sys.stdin.readline

N,M = map(int, input().split())

L=list(map(int, input().split()))
L.sort()

for i in itertools.permutations(L,M):
   for j in i:
      print(j, end=' ')
   print()