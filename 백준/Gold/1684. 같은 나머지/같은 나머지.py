import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int, input().split()))

L.sort()
s = set()
for i in range(n-1):
    s.add(L[i+1]-L[i])
    
s=list(s)

def gcd(a,b):
    if a<b:
        b,a = a,b
    if b==0:
        return a
    return(gcd(b, a%b))
res = s[0]
for i in range(1,len(s)):
    res = gcd(res,s[i])
    
print(res)