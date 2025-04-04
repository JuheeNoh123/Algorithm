import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline


a = input().strip()

dp=[0 for _ in range(len(a)+1)]
dp[0]=1
a = '0'+a
dp[1]=1
for i in range(2,len(a)):
    if a[i]!='0':
        dp[i]=dp[i-1]
    if int(a[i-1]+a[i]) <=34 and a[i-1]!='0':
        dp[i] += dp[i-2]

    
        

print(dp[-1])