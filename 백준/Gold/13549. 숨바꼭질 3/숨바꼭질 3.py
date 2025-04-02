import sys
from collections import deque
from itertools import permutations;
input = sys.stdin.readline

A = [100001] * 100001
visited = [0] * 100001
# 4 6은 왜 1인가?
# 10 14가 왜 3인가?
def sol(start,end):
    A[start]=0
    visited[start]=1
    queue=deque([start])
    while queue:
        x = queue.popleft()
        dx=[x,-1,1]
        if x==end:
            return
        for i in dx:
            nx = x+i
            if 0<=nx and nx<100001 and not visited[nx]:
                if i==x:
                    A[nx]=A[x]
                else:
                    A[nx]=A[x]+1
                queue.append(nx)
                visited[nx]=True
                #print(x,A[:21])
s,e = map(int, input().split())
sol(s,e)      
print(A[e])