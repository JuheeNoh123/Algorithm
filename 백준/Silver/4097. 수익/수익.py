import sys
input = sys.stdin.readline
n=int(input())
while n!=0:
    L=[]
    dp=[0]*n
    for i in range(n):
        a=int(input())
        L.append(a)
    L.append(0)
    dp[0]=L[0]
    for i in range(1,n):
        dp[i]=max(dp[i-1]+L[i],L[i])
        #print(dp)
    n=int(input())
    print(max(dp))