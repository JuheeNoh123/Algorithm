a = int(input())
L = list(map(int, input().split()))
cnt = 0
while sum(L) != 0:
    L.sort(reverse=True)
    L[0] -= 1
    if len(L)>=2 and L[1] != 0:
        L[1] -= 1
    
    cnt += 1

if cnt > 1440:
    print(-1)
else:
    print(cnt)