import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int, input().split())

L=list(map(int, input().split()))
L=L*2
#print(L)
res = [0 for _ in range(n*2)]
res[0]=L[0]
for i in range(1,n*2):
    res[i] = res[i-1]+L[i]
#print(res)
ans = [0 for _ in range(n*2)]
ans[k-1]=res[k-1]
for i in range(k,n+k-1):
    ans[i] = res[i]-res[i-k]
print(max(ans))