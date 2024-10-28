import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
      N, M = map(int, sys.stdin.readline().split())
      L = list(map(int, sys.stdin.readline().split()))
      result = 1
      while L:
            if L[0]<max(L):
                  L.append(L.pop(0))
            else:
                  if M==0:
                        break
                  L.pop(0)
                  result += 1
                  
                  
            M = M-1 if M!=0 else len(L)-1
      print(result)