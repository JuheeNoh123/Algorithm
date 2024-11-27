import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    dp = [1 for _ in range(101)]
    dp[4],dp[5] = 2,2
    dp[6]=3
    dp[7]=4
    dp[8]=5
    n = int(input())
    for i in range(9, n+1):
        dp[i] = dp[i-1]+dp[i-5]
    print(dp[n])
    