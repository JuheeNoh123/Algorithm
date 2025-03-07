from sys import stdin
from collections import deque

input = stdin.readline

T  = int(input())
def binarySearch(idx_s,idx_e,t):
    
    s=idx_s
    e=idx_e
    m=(s+e)//2
    if s<=e:
        if note1[m]<t:
            s=m+1
            return binarySearch(s,e,t)
        elif note1[m]>t:
            e=m-1
            return binarySearch(s,e,t)
        else:
            return 1    #값이 있을때
    else:
        return 0       #값이 없을때때

for i in range(T):
    N = int(input())
    note1 = list(map(int, input().split()))
    note1.sort()
    M = int(input())
    note2= list(map(int,input().split()))
 
    for t in note2:
        print(binarySearch(0,N-1,t))
    
