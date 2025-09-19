import sys
from itertools import permutations
input = sys.stdin.readline
t = int(input())


for i in range(t):
    q = int(input())
    n = q%28
    if n==0:
        n=2
    elif n>15:
        n = 30-n%28 #(2+28)-n%28
    #print(n)
    b = str(bin(n))[2:]
    #print(b)
    if len(b)<4:
        b = '0'*(4-len(b))+b
    #print(b)
    ans = ''
    for j in range(4):
        #print(b[j])
        if b[j]=='0':
            ans += 'V'
        else:
            ans+='딸기'
    print(ans)