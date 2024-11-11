import sys
input = sys.stdin.readline
L = [0]*301
dp = [0]*301
N = int(input())
for i in range(1,N+1):
    L[i] = int(input())
dp[1] = L[1]
dp[2] = L[1] + L[2]
dp[3] = max(L[1]+L[3], L[2]+L[3])

for i in range(4,N+1):
    dp[i] = max(L[i]+dp[i-2], L[i]+L[i-1]+dp[i-3])
print(dp[N])
    