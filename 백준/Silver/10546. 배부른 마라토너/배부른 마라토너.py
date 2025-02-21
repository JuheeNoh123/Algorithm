import sys
input = sys.stdin.readline

n=int(input())
members = {}

for i in range(n):
    name=input().strip()
    if name in members:
        members[name]+=1
    else:
        members[name]=1
    

#print(members)

for i in range(n-1):
    name=input().strip()
    members[name]-=1

for i in members:
    if members[i]==1:
        print(i)
        break