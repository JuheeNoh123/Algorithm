import sys
input = sys.stdin.readline

s = input().strip()
L=[]
minusList = []
c= ''
cnt=0

for i in range(len(s)):
    if 48<=ord(s[i])<=57:
        c+=s[i]
    else:
        cnt+=1
        L.append(int(c))
        c=''
        if s[i]=='-':
            minusList.append(cnt)
    if i==len(s)-1:
        L.append(int(c))
        
minusList.append(len(L))        
newL = []
if len(minusList)==1:   #마이너스 1개일때 (리스트 인덱스 초과 오류때메)
    minus = minusList[0]
    newL=[L[0]]
    for i in range(minus,len(L)):
        newL.append(-L[i])
else:
    for i in range(minusList[0]):
        newL.append(L[i])
    for i in range(1,len(minusList)):
        minus = minusList[i-1]
        nextMinus = minusList[i]
        #print(minus, nextMinus)
        for j in range(minus,nextMinus):
            newL.append(-L[j])
        
        
# print(minusList)
# print(L)
# print(newL)
            
        
if len(minusList)==1:
    print(sum(L))
else:
    print(sum(newL))    
