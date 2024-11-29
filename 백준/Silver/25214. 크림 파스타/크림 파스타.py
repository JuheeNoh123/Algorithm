import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int,input().split()))

dp = [0]*n
min1 = num[0]
max1 = num[0]
for i in range(1,n):
    if min1>num[i]:
        min1 = num[i]
    # if max1<num[i]:
    #     max1 = num[i]
    #print(min1)
    
    dp[i] = max(num[i]-min1,dp[i-1])
print(*dp)