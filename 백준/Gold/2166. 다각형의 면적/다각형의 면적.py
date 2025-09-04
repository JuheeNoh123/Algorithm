import sys
input = sys.stdin.readline

n = int(input())
L=[]
for i in range(n):
    a,b = map(int, input().split())
    if i==0:
        x,y = a,b
    L.append((a,b))

L.append((x,y))
s=0
for i in range(n):
    s += L[i][0]*L[i+1][1]
for i in range(1,n+1):
    s-=L[i][0]*L[i-1][1]
if s<0:
    s*=-1
print(f"{s/2:.1f}")