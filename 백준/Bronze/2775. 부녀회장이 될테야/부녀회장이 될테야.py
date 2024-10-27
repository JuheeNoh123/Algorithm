T = int(input())

for t in range(T):
      L = [[i for i in range(1,15)]]
      K = int(input())
      N = int(input())
      for i in range(1, K+1):
            L.append([0]*N)
            for j in range(N):
                  for k in range(j+1):
                        L[i][j] += L[i-1][k]
            
      print(L[K][N-1])