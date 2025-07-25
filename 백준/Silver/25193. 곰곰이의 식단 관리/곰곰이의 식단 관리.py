import sys
input = sys.stdin.readline
'''
c = 4 : 2 -> 1
e = 2 : 1 -> 0
4/3 = 1.33 
ceccec
ans : 2

c = 4 : 2
e = 1 : 0
4/2
ans : 2

c = 4
4/4=1
e = 3
cececec
ans : 1

c 5
5/4 = 1.25
e 3
caccacac
ans : 2
'''


n = int(input())
s = input().strip()
cntc = 0
cnte = 0
for i in s:
    if i=='C':
        cntc+=1
    else:
        cnte+=1
if cnte!=0:
    ans = cntc/(cnte+1)

    if int(ans)==ans:
        print(int(ans))
    else:
        print(int(ans)+1)
else:
    print(n)