import sys 
input = sys.stdin.readline


a,b,d = map(int,input().split())
L=[i for i in range(1,b+1)]
L[0]=-1
for i in range(int(b**0.5)):
    if L[i]==-1:
        continue
    for j in range(i,b,L[i]):
        #print(L[j], L[i])
        if L[j]==-1 or j==i:
            continue
        #if L[j]%L[i]==0:
        L[j]=-1
        #print(L)
#print(L)
cnt = 0
for i in L[a-1:b]:
    if i==-1:
        continue
    if str(d) in str(i):
        cnt += 1
print(cnt)