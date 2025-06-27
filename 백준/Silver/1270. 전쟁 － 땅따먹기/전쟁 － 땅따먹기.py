import sys
input = sys.stdin.readline


n = int(input())

for _ in range(n):
   dic = {}
   L = list(map(int,input().split()))
   ban = L[0]//2
   for j in range(1,L[0]+1):
      if dic.get(L[j])==None:
         dic[L[j]]=1
      else:
         dic[L[j]]+=1
   #print(dic)
   cnt1 = 0
   cnt2=0
   for k in dic:
      if dic[k]>ban:
         print(k)
      elif dic[k]==ban:
         cnt1 +=1
      else:
         cnt2+=1
   #print(cnt1, cnt2)
   if cnt2 == len(dic) or cnt1 ==len(dic) or cnt1+cnt2==len(dic):
      print("SYJKGW") 
   
         
   