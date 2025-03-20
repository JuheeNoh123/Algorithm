import sys
input = sys.stdin.readline

n = int(input())


L=list(map(int, input().split()))
dp=L
dp2=L
#최댓값
for i in range(1,n):
    L=list(map(int, input().split()))
    L2=[i for i in L]
    for j in range(3):
        if j==0:
            max_num=max(dp[0],dp[1])
            min_num=min(dp2[0],dp2[1])
        elif j==1:
            max_num=max(dp)
            min_num=min(dp2)
        else:
            max_num=max(dp[1],dp[2])
            min_num=min(dp2[1],dp2[2])
        #print(max_num,min_num)
        L[j]+=max_num
        L2[j]+=min_num
        
    dp=L
    dp2=L2
print(max(dp),min(dp2))