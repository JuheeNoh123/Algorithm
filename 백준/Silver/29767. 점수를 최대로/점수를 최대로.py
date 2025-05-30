import sys
input = sys.stdin.readline

n,k = map(int,input().split())
L =list(map(int,input().split()))
s=[0 for _ in range(n)]
s[0]=L[0]
for i in range(1,n):
   s[i] = s[i-1]+L[i]
#print(s)

s.sort(reverse=True)
print(sum(s[:k]))