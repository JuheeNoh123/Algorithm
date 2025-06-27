import sys
input = sys.stdin.readline


n1,n2 = map(int, input().split())
s1 = input().strip()
s2 = input().strip()
T = int(input())
L = []
for i in s1[::-1]:
   L.append((1,i))

for i in s2:
   L.append((2,i))
#print(L)
cnt = 0

def change(a,b):
   L[a],L[b] = L[b],L[a]

for _ in range(T):
   index=[]
   for idx in range(len(L)-1):
      if L[idx][0]==2:
            continue
      if L[idx][0] != L[idx+1][0] and not idx in index:
         
         #L[idx],L[idx+1] = L[idx+1],L[idx]
         index.append(idx)
         index.append(idx+1)
         #print(index)   #현재 턴에 바꿔야할 개미의 인덱스
   # print('---------')
   # print(index)  
   for i in range(0,len(index),2):
      change(index[i],index[i+1])
      #print(L)
ans = ''      
for i in L:
   ans += i[1]
print(ans)