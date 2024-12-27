import sys
input = sys.stdin.readline

n=int(input())
L=[0 for _ in range(51)]
L[0],L[1]=1,1

for i in range(2,n+1):
    L[i]=L[i-1]+L[i-2]+1

print(L[n]%1000000007)