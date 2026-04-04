num=1
while True:
    s = int(input())
    if s==0:
        break
    L = []
    for i in range(s):
        L.append(input())
    dic = [0 for _ in range(s)]
    for i in range(2*s-1):
        n, ab = input().split()
        if dic[int(n)-1]==0:
            dic[int(n)-1]=1
        else:
            dic[int(n)-1]=0
        #print(dic)
    for i in range(s):
        if dic[i]==1:
            print(num, L[i])
    num+=1