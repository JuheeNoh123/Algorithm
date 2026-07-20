def check(dir,dist, curi, curj, w, h, park):
    ni, nj= curi, curj
    di, dj = [-1,1,0,0],[0,0,-1,1] #n,s,w,e
    for i in range(dist):
        #print(ni, nj)
        if dir=='N':
            ni,nj= ni+di[0], nj+dj[0]
        elif dir=='S':
            ni,nj= ni+di[1], nj+dj[1]
        elif dir=='W':
            ni,nj= ni+di[2], nj+dj[2]
        elif dir=='E':
            ni,nj= ni+di[3], nj+dj[3]
        if ni>=h or ni<0 or nj<0 or nj>=w or park[ni][nj]=='X':
            return False
        
            
        #print(ni, nj)
    return [ni,nj]
def solution(park, routes):
    answer = [0,0]
    h = len(park)
    w = len(park[0])
    s=0
    for i in range(h):
        for j in range(w):
            if park[i][j]=='S':
                s=(i,j)
    #print('s',s)
    di, dj = [-1,1,0,0],[0,0,-1,1] #n,s,w,e
    curi, curj= s[0], s[1]
    for route in routes:
        dir, dist = route.split()
        dist = int(dist)
        #print(route)
        L = check(dir, dist, curi, curj,w,h, park)
        #print("L",L)
        if not L:
            continue
        curi, curj = L[0], L[1]
        
        
        
    answer[0], answer[1] = curi,curj
    return answer