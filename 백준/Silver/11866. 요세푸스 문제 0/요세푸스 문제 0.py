N, K = map(int, input().split())
L = [i for i in range(1,N+1)]
res = []
p = K-1
for i in range(N):
      if p>=len(L):
            p=p%len(L)
      res.append(str(L.pop(p)))
      p+=K-1
str='<'
str += ', '.join(res)
str += '>'
print(str)
      