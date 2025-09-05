import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    m=0
    idx=0
    s=0
    L=[]
    
    for i in range(1,n+1):
        v = int(input())
        L.append(v)
        s+=v
    for i in range(n):
        if L[i]>=m:
            m=L[i]
            idx=i
            
    avg = s/2

    if L.count(m)==1:#최다 득표자 한명
        if m>avg: #과반수 초과
            print(f"majority winner {idx+1}")
        else: #과반수 이하
            print(f"minority winner {idx+1}")
    else:
        print("no winner")
    