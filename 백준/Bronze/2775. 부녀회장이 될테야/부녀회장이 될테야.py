T = int(input())

for t in range(T):
      K = int(input())
      N = int(input())
      L = [i for i in range(1,N+1)]
      for i in range(K):
            for j in range(1,N):
                  L[j] += L[j-1]
            
      print(L[-1])