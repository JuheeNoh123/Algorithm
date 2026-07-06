import copy
def solution(friends, gifts):
    answer = 0
    get = {}
    give = {}
    f = {}
    g= {}
    for i in friends:
        f[i]=0
        g[i]=[0,0,0]
    for i in friends:    
        get[i]=copy.deepcopy(f)
        give[i]=copy.deepcopy(f)
    
    for i in gifts:
        a,b = i.split()
        give[a][b]+=1
        get[b][a]+=1
    
    #print(give)
    #print(get)
    mm={}
    for i in friends:
        mm[i] = [0,0,0]


    for k in give:
        #print(k)
        give_gifts = 0
        for p in give[k]:
            #print(give[k][p])
            give_gifts+=give[k][p]
        mm[k][0] = give_gifts
        get_gifts=0
        for p in get[k]:
            get_gifts+=get[k][p]
        mm[k][1] = get_gifts
        mm[k][2]=mm[k][0]-mm[k][1]
    #print(mm)
    res = {}
    visited = [[0]*len(friends) for _ in range(len(friends))]
    for i in friends:
        res[i] = 0
        
    idx=0
    goal=1
    for k in give:
        idx=0
        for j in give[k]:
            if idx<goal:
                idx+=1
                continue
            #print(k,j)
            if give[k][j] > give[j][k]:
                res[k]+=1
                
            elif give[k][j] < give[j][k]:
                res[j]+=1
            else:
                if mm[k][2] < mm[j][2]:
                    res[j]+=1
                elif mm[k][2] > mm[j][2]:
                    res[k] +=1
                
        goal+=1 
        #print(res) 
    
    
    for i in res:
        if res[i]>answer:
            answer=res[i]
    return answer