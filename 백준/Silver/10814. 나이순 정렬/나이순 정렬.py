N = int(input())
L = []
for i in range(N):
      age, name = input().split()
      L.append((int(age), name))
      
L.sort(key = lambda x : x[0])

for age, name in L:
      print(age, name)
