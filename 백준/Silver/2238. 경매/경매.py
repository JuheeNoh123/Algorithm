import sys

input = sys.stdin.readline

u,n = map(int, input().split())
L=  [[] for _ in range(u+1)]
for i in range(n):
    name, cost = input().strip().split()
    cost = int(cost)
    L[cost].append(name)
min_people=10001
min_id=0
flag=0
#print(L)
for i in range(1,u+1):
    
    if len(L[i])==1:
        print(L[i][0],i)
        flag=1
        break
    if min_people>len(L[i]) and len(L[i])!=0:
        min_people = len(L[i])
        min_id = i
#print(min_people, min_id)
if flag==0:
    print(L[min_id][0],min_id)
        