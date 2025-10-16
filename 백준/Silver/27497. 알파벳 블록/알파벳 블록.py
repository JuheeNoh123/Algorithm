import sys
from collections import deque
input = sys.stdin.readline

s = deque()
n = int(input())
pre=[]
for _ in range(n):
    i = input().strip()
    if len(i)>1:
        if i[0]=='1':
            s.append(i[2:])
            pre.append(1)
        else:
            s.appendleft(i[2:])
            pre.append(2)
    else:
        if len(pre)==0:
            continue
        elif pre[-1]==1:
            s.pop()
            pre.pop()
        elif pre[-1]==2:
            s.popleft()
            pre.pop()
        
ans = ''.join(s)
if len(ans)==0:
    print(0)
else:
    print(ans)