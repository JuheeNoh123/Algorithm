import sys
input = sys.stdin.readline

N, K = map(int,input().split())
L = []
for _ in range(N):
    A = int(input())
    L.append(A)
L.sort(reverse=True)
cnt = 0
for i in L:
    if K>=i:
        cnt += K//i
        K -= i*(K//i)
    
print(cnt)
    