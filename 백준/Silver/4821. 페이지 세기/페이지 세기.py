import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n==0:
        break
    sum=0
    page=[]
    L=list(input().strip().split(','))
    for i in L:
        a = i.split('-')
        #print(a)
        if len(a)==1:
            if int(a[0])<=n:
                page.append(int(a[0]))
        else:
            if int(a[1])<=n:
                for i in range(int(a[0]),int(a[1])+1):
                    page.append(i)
            else:
                for i in range(int(a[0]),n+1):
                    page.append(i)
        
        
    #print(page)
    ans=set(page)
    print(len(ans))