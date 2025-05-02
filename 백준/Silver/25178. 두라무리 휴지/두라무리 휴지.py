import sys

input = sys.stdin.readline


n = int(input())
s1 = input().strip()
s2 = input().strip()
can="YES"


newS1 = ''
newS1dic = {}
newS2=''
newS2dic = {}
for i in s1:
    if newS1dic.get(i) == None:
        newS1dic[i]=1
    else:
        newS1dic[i]+=1
    if not i in 'aeiou':
        newS1+=i
for i in s2:
    if newS2dic.get(i) == None:
        newS2dic[i]=1
    else:
        newS2dic[i]+=1
    if not i in 'aeiou':
        newS2+=i


for k in newS1dic:
    if newS1dic[k]!=newS2dic.get(k):
        can = "NO"
        break
    
if s1[0]!=s2[0] or s1[-1]!=s2[-1]:
    can = "NO"
      
if newS1!=newS2:
    can = "NO"
    
print(can)
