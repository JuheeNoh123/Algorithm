import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def applyCommand(n, command):
    if command == "D":
        return (n * 2) % 10000
 
    if command == "S":
        return (n - 1) % 10000
 
    if command == "L":
        return (10 * n + (n // 1000)) % 10000
 
    if command == "R":
        return (((n % 10) * 1000) + (n // 10)) % 10000
    
    
def bfs(n):
    q = deque()
    q.append((n,""))
    
    visited[n] = True
    
    while q:
        n, res = q.popleft()
        
        if n==b:
            return res
        for command in commands:
            newn = applyCommand(n,command)
            
            if not visited[newn]:
                visited[newn] = True
                q.append((newn,res+command))
    
T = int(input())
commands = ['D',"S",'L','R']

for _ in range(T):
    a,b = map(int,input().split())
    visited = [False]*10000
    
    print(bfs(a))