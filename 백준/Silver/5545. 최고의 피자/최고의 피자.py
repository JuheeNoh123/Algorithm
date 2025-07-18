import sys

input = sys.stdin.readline


n = int(input())
a,b = map(int,input().split())
c = int(input())
d=[0]
for i in range(n):
    d.append(int(input()))
    
d.sort(reverse=True)
#print(d)
s=c
w=a
k=-1
for i in range(n+1):
    if i==n:
        s=c
        w=a
    else:
        s+=d[i]
        w += b
    #print(s,w)
    k = max(k,s//w)
    #print(k)
print(k)