import sys
input = sys.stdin.readline

n = int(input())
L = [0 for _ in range(0,367)]
for _ in range(n):
    s,e = map(int, input().split())
    for i in range(s,e+1):
        L[i]+=1
#print(L)
h = 0
cnt = 0
ans = 0
for i in range(367):
    if L[i]!=0:
        cnt+=1
        h = max(h, L[i])
    else:
        ans += h*cnt
        cnt = 0
        h=0

    
print(ans)