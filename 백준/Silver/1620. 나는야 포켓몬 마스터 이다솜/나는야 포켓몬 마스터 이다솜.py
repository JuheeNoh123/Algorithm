import sys
input = sys.stdin.readline
N,M = map(int,input().split())
L={}
L2 = {}
for i in range(N):
    name = input().strip()
    L[i+1] = name
    L2[name] = i+1
for i in range(M):
    q = input().strip()
    if 49<=ord(q[0]) and ord(q[0])<=57:
        print(L[int(q)])
    else:
        print(L2[q])
