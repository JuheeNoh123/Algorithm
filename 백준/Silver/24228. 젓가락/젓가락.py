import sys
from collections import deque
input = sys.stdin.readline


N,R=map(int, input().split())

print(N+1+(R-1)*2)