import sys
input = sys.stdin.readline

N,M,V = map(int, input().split())
k=N-V+1
L=list(map(int,input().split()))
L2=L[V-1:]
for i in range(M):
    q = int(input())
    if q<N:
        print(L[q])
    else:
        q=(q-(V-1))%k
        print(L2[q])