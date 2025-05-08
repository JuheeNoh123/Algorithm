import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
real = input().strip()
if real[0]=='0':
    for i in range(m):
        L = list(map(int, input().split()))
    print(m)
else:
    reals = real.split()
    len_reals = int(real[0])
    reals = reals[1:]
    queue = deque()
    for i in range(len_reals):
        queue.append(int(reals[i]))        
        

    parties = [0] * m

    for i in range(m):
        partyone = list(map(int, input().split()))
        partyone = partyone[1:]
        parties[i] = partyone
    #print(reals)
    #print(parties)


    while queue:
        real_p = queue.popleft()
        for i in range(m):
            if real_p in parties[i]:
                #print(real_p)
                for j in range(len(parties[i])):
                    if real_p == parties[i][j]:
                        continue
                    queue.append(parties[i][j])
                parties[i]=[]
        #print(queue)
    cnt = 0
    for i in range(m):
        if parties[i]:
            cnt +=1
    print(cnt)
        