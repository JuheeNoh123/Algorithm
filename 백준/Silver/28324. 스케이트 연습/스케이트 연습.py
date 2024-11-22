import sys
input = sys.stdin.readline

n = int(input())
V = list(map(int,input().split()))
V[-1] = 1
for i in range(len(V)-2,-1,-1):
    if V[i+1]+1 < V[i]:
        V[i]=V[i+1]+1
print(sum(V))