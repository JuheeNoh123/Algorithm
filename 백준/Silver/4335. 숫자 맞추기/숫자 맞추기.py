import sys
from collections import deque
input = sys.stdin.readline

olly = int(input())
s=[0,1,2,3,4,5,6,7,8,9,10]
while olly!=0:
    stan = input().strip()
    if stan=='too high': #a보다 더 작은 수
        for i in range(olly,11):
            s[i]=0
        #print(s)
    elif stan=='too low':
        for i in range(olly+1):
            s[i]=0
        #print(s)
    else:
        if not s[olly]:
            print("Stan is dishonest")
        else:
            print("Stan may be honest")
        s=[0,1,2,3,4,5,6,7,8,9,10]
    olly=int(input())