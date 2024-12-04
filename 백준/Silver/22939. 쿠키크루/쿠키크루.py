import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
field = [[] for _ in range(n)]
crew = ['Assassin','Healer','Mage','Tanker']
toppingKinds= ['J','C','B','W']
home = [0,0]
cookie = [0,0]
topping = [[] for _ in range(4)]

def dist(a,b):
    #print(a,b)
    return abs(a[0]-b[0])+abs(a[1]-b[1])


for i in range(n):
    field[i] = input().strip()
    for j in range(n):
        if field[i][j]=="H":
            home = [i,j]
        if field[i][j]=="#":
            cookie = [i,j]
        for k in range(4):
            if field[i][j]==toppingKinds[k]:
                topping[k].append([i,j])
    min = 10000
    type = 0
for k in range(4):
    perm = permutations(topping[k],3)
    
    for p in perm:
        #print(p)
        d = dist(home,p[0])+dist(p[0],p[1])\
            +dist(p[1],p[2])+dist(p[2],cookie)
        if min>d:
            min = d
            type = k
        #print(d, type)
        
print(crew[type])