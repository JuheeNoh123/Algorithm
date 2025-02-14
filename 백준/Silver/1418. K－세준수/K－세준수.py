import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

L = [i for i in range(1,N+1)]

for i in range(1,int(N**0.5)):
    if L[i]==0:
        continue
    for j in range(i*2+1,N):
        if L[j]==0:
            continue
        if L[j] % L[i]==0:
            #print(L[j])
            L[j]=0
            

cnt=0
L=set(L)
L=list(L)
L.sort()
#print(L)
for i in range(1,N+1):
    A=True
    for j in L:
        if j==0:
            continue
        if i%j==0:
            if j>K:
                A=False
                break
                #print(i, A)
    if A:
        cnt+=1
        #print(cnt)           
print(cnt)