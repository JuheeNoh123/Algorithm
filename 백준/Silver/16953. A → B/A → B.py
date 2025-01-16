import sys
from collections import deque
input = sys.stdin.readline

A, B= map(int,input().split())


def bfs():
    
    queue = deque([(A,1)])
    while queue:
        num,cnt=queue.popleft()
        if num==B:
            print(cnt)
            return
        n1 = int(str(num)+'1')
        n2 = num*2
        if n1<=B:
            queue.append((n1,cnt+1))
            
        if n2<=B:
            queue.append((n2,cnt+1))

    print(-1)
    
bfs()

