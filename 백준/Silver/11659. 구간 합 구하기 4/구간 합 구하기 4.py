import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L = list(map(int, input().split()))
dp = [0]*(N+1)
for i in range(N):
    dp[i+1] = L[i] + dp[i]

#print(dp)
for _ in range(M):
    sum = 0
    i,j = map(int,input().split())
    print(dp[j]-dp[i-1])