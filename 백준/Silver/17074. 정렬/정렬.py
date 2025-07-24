import sys
input = sys.stdin.readline

n = int(input())
L=list(map(int,input().split()))
r=-1
cnt=0
for i in range(n-1):
    if L[i]>L[i+1]:
        r=i
        cnt += 1
res=0
if cnt==0:
    print(n)
elif cnt>1:
    print(0)
else:
    
    if r+2<n:
        if L[r]<=L[r+2]:  #L[r+1] 삭제
            res+=1
        # if r==0:
            
    elif r+1==n-1: #맨 마지막 요소 삭제
        res+=1
    if r-1>=0:
        if L[r-1]<=L[r+1]:  #L[r] 삭제
            res+=1
    else:
        res+=1
    print(res)
