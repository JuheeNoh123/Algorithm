import sys
input = sys.stdin.readline
N,M = map(int, input().split())

L = list(map(int, input().split()))
L.append(0)
L.append(1000000001)
L.sort()
def binarySearch(s,e,t):
    while s<=e:
        m = (s+e)//2
        if t<L[m]:
            e=m-1
        elif t>L[m]:
            s=m+1
        else:
            return m
    return e
    
def binarySearch2(s,e,t):
    while s<=e:
        m = (s+e)//2
        if t<L[m]:
            e=m-1
        elif t>L[m]:
            s=m+1
        else:
            return m
    return s
for i in range(M):
    a,b = map(int, input().split())
    x = binarySearch2(0,N+1,a)
    y = binarySearch(0,N+1,b)
    if y-x<0:
        print(0)
    else:
        print(y-x+1)