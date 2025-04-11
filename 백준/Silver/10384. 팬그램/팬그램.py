import sys

input = sys.stdin.readline

n = int(input())


for i in range(n):
    d = {}
    cnt = 0
    string = input().strip()
    for j in string:
        if ord("A")<=ord(j)<=ord("Z"):
            #print(j)
            if d.get(j)==None:
                cnt += 1
                d[j]=1
            else:
                d[j]+=1
        elif ord('a')<=ord(j)<=ord('z'):
            J = chr(ord(j)-32)
            #print(J)
            if d.get(J)==None:
                d[J]=1
            else:
                d[J]+=1
        else:
            continue
    #print(d)
    #print(len(d))
    if len(d)==26:
        ans = 1e9
        for k in d:
            ans = min(ans,d[k])
            if ans==1:
                catagory = "Pangram!"
            elif ans==2:
                catagory = "Double pangram!!"
            else:
                catagory = "Triple pangram!!!"
        
        print(f"Case {i+1}: {catagory}")
    else:
        print(f"Case {i+1}: Not a pangram")
        