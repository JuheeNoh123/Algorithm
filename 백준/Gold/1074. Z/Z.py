import sys

input = sys.stdin.readline


N, r, c = map(int, input().split())
ans = 0
pos = []
for i in range(N-1,-1,-1):
    if r<2**i and c<2**i:#1사분면
        ans = ans
    elif r<2**i and c>=2**i:#2사분면
        ans += 2**(2*i)
        c -= 2**i
    elif r>=2**i and c<2**i:#3사분면
        ans += 2*(2**(2*i))
        r-=2**i
        
    else:               #4사분면
        ans += 3*(2**(2*i))
        r-=2**i
        c-=2**i

print(ans)