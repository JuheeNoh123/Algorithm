import math

a = int(input())
L = list(map(int, input().split()))

cnt = max(max(L),math.ceil(sum(L)/2))

if cnt>1440:
    print(-1)
else:
    print(cnt)