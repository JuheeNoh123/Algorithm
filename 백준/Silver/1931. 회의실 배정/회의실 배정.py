import sys
input = sys.stdin.readline

n = int(input())
L=[]
for i in range(n):
    a,b=map(int, input().split())
    L.append((a,b))

L2 = sorted(L,key= lambda y:(y[1],y[0]))

# print(L2)

#print(L2)
cnt=0
end=0
for i in range(n):
    #print(end,L2[i][0])
    if end<=L2[i][0]:
        end=L2[i][1]
        cnt+=1
print(cnt)