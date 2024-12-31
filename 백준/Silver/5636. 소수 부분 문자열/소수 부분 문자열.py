import sys
input = sys.stdin.readline


sosoo=[i for i in range(0,100001)]
for i in range(2,101):
    if sosoo[i]==0:
        continue
    for j in range(i+1, 100001):
        if sosoo[j]==0:
            continue
        if sosoo[j]%i==0:
            sosoo[j]=0   


while True:
    L=set()
    n=input().strip()
    if n=="0":
        break
    for i in range(len(n)):
        for j in range(i+1):
            L.add(int(n[j:i+1]))
    L=list(L)
    
    max=0
    for i in range(len(L)):
        if L[i]<=100000:
            if sosoo[L[i]]!=0 and sosoo[L[i]]>max:
                max=sosoo[L[i]]
    print(max)
