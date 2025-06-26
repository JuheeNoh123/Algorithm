import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)





n,m = map(int, input().split())
if n<m:
   x = 1
   for i in range(1,n+1):
      x *= i
      x %= m
   print(x)
else:
   print(0)
