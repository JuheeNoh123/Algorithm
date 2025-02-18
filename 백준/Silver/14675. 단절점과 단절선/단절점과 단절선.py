import sys
input = sys.stdin.readline
N = int(input())
L = [[] for _ in range(N+1)] 
# print(L)
for i in range(N-1):
    a,b = map(int, input().split())
    L[a].append(b)
    L[b].append(a)

q = int(input())
for i in range(q):
    a,b = map(int, input().split())
    if a==2:
        print("yes")
    else:
        if len(L[b])==1:
            print("no")
        else:
            print("yes")