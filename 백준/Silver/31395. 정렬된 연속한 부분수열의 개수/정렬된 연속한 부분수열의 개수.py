import sys
input = sys.stdin.readline

n = int(input())

A=list(map(int,input().split()))
L = [0]*n
L[0]=1
#cnt=0
for i in range(1,n):
    if A[i]>A[i-1]:
        L[i]=L[i-1]+1
    else:
        L[i]=1

    
    
print(sum(L))