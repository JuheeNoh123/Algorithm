import sys
input = sys.stdin.readline

p, m = map(int, input().split())
L=[]
def makeroom(I,N):
    for i in L:
        start_lev = i[0][0]-10
        end_lev=i[0][0]+10
        if start_lev<=I<=end_lev:
            if len(i)<m:
                i.append((I,N))
                break
            else:
                continue
    else:
        room=[(I,N)]
        L.append(room)
        
    
for i in range(p):
    I, N = input().split()
    I=int(I)
    makeroom(I,N)
    #print(L)
    
for i in L:
    #print(i)
    i.sort(key=lambda x:x[1])
    #print(i)
    if len(i)==m:
        print("Started!")
    else:
        print("Waiting!")
    for j in i:
            print(j[0],j[1])