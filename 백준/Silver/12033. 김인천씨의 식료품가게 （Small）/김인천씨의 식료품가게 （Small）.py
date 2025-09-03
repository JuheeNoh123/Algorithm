import sys
input = sys.stdin.readline

T = int(input())

for i in range(1,T+1):
    N = int(input())
    L = list(map(int, input().split()))
    idx = []
    for j in range(len(L)):
        for k in range(j):
            if L[j]==0:
                continue
            if L[j]*0.75==L[k]:
                #print(L[k])
                idx.append(str(L[k]))
                L[j] = 0
                L[k]=0
    s =' '.join(idx)
    print("Case #"+ str(i)+ ": "+s)