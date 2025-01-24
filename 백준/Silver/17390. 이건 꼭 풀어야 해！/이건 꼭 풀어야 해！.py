import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
B = list(map(int, input().split()))
B.sort()
dp=[0,B[0]]

for i in range(1,N):
    dp.append(B[i]+dp[i])
    
#print(dp)
for i in range(Q):
    L,R = map(int, input().split()) 
    print(dp[R]-dp[L-1])