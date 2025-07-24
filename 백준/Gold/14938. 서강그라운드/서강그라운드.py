import sys
input = sys.stdin.readline
INF = sys.maxsize
n,m,r = map(int, input().split())
items = list(map(int, input().split()))
L=[[INF]*(n+1) for _ in range(n+1)]
for i in range(r):
    a,b,l = map(int, input().split())
    L[a][b]=l
    L[b][a]=l
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            L[i][j]=0
            
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            L[i][j] = min(L[i][j],L[i][k]+L[k][j])
#print(L)
s=0
ans=[]
for i in range(1,n+1):
    s=items[i-1]
    for j in range(1,n+1):
        if i==j:
            continue
        if L[i][j]<=m:
            s+=items[j-1]
        #print(s)
    ans.append(s)
    
print(max(ans))