import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
d = deque()
max_len=0
min_num=100001
for i in range(n):
    A = input().strip()
    if A[0]=='1':
        d.append(A[2:])
    else:
        d.popleft()
    #print(d)
    if max_len==len(d):
        #max_len=len(d)
        if int(d[-1])<min_num:
            min_num=int(d[-1])
    elif max_len<len(d):
        max_len=len(d)
        min_num=int(d[-1])
print(max_len,min_num)

