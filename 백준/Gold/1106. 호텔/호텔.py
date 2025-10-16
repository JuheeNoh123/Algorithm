import sys
import time
input = sys.stdin.readline

c,n = map(int, input().split())
cost_list = []
for i in range(n):
    cost, num = map(int, input().split())
    cost_list.append([cost, num])

dp=[1e7 for i in range(c+100)]
dp[0]=0
for cost,num_people in cost_list:
    for i in range(num_people,c+100):
        dp[i] = min(dp[i-num_people]+cost, dp[i])

print(min(dp[c:]))