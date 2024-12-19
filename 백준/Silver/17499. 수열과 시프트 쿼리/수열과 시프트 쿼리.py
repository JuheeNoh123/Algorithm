import sys
from collections import deque
input = sys.stdin.readline

d = deque()
n,q = map(int,input().split())
L = list(map(int,input().split()))
for i in L:
    d.append(i)
#print(*d)
for i in range(q):
    req = list(map(int, input().split()))
    if req[0]==1:
        d[req[1]-1] += req[2]
        #print(d)
    elif req[0]==2:
        
        d.rotate(req[1])
        #print(d)
    elif req[0]==3:
        d.rotate(-req[1])
        #print(d)

print(*d)