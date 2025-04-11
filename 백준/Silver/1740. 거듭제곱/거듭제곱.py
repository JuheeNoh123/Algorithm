import sys

input = sys.stdin.readline

n = int(input())
bit = bin(n)
bit = bit[2:]
m = 1
ans = 0
for i in range(len(bit)-1,-1,-1):
    if bit[i]=='1':
        ans += m
    m *= 3
    
    
print(ans)