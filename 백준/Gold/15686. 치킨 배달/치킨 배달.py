import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
L =[list(map(int, input().split())) for _ in range(n)]
home = []
chicken = []
for i in range(n):
    for j in range(n):
        if L[i][j]==1:
            home.append((i,j))
        elif L[i][j]==2:
            chicken.append((i,j))
#print(home, chicken)
tmp = []
res =[]     
def backtrack(s, d):
    if d==m:
        res.append(tmp[:])
        #print('res',res)
        return
    for i in range(s, len(chicken)):
        tmp.append(chicken[i])
        #print(tmp)
        backtrack(i+1,d+1)
        tmp.pop()
backtrack(0,0)
#print(res)
ct = []
for i in res:
    sum=0
    for a,b in home:
        min_chick = 999999999999
        for x,y in i:
            d = abs(a-x)+abs(b-y)
            if min_chick>d:
                min_chick = d
        
        sum += min_chick
    ct.append(sum)
    

print(min(ct))