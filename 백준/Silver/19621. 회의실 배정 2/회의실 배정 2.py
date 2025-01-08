import sys
input = sys.stdin.readline

n = int(input())
L=[]
for i in range(n):
    a,b,c = map(int, input().split())
    L.append((a,b,c))
    
L2 = sorted(L, key=lambda y:(y[1],y[0]))
dp=[0]*n
dp[0] = L[0][2]
for i in range(1,n):
    dp[i] = max(dp[i-1], dp[i-2]+L[i][2])

print(dp[-1])