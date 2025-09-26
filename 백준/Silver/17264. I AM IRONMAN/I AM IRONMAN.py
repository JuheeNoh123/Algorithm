import sys

input = sys.stdin.readline

n, p = map(int, input().split())
w,l,g = map(int, input().split())
h={}

for i in range(p):
    name, case = input().split()
    h[name]=case
score=0
flag=False
for i in range(n):
    name = input().strip()
    if h.get(name)==None:
        score -= l
        if score<0:
            score=0
    elif h[name]=='L':
        score -= l
        if score<0:
            score=0
    else:
        score += w
        
    if score>=g:
        flag=True
    #print(score)
if flag:
    print("I AM NOT IRONMAN!!")
else:
    print("I AM IRONMAN!!")