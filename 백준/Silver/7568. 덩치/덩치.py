N = int(input())
L=[]
order = [1]*N
for i in range(N):
      X, Y = map(int, input().split())
      L.append([X,Y])
for i in range(N):
      for j in range(N):
            if i==j:
                  continue
            if L[i][0] < L[j][0] and L[i][1] < L[j][1]:
                  order[i]+=1

print(*order)