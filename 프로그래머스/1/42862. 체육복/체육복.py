def solution(n, lost, reserve):
    answer = 0
    d={k:1 for k in range(1,n+1)}

    for i in reserve:
        d[i]=2
    for i in lost:
        if d[i]==2:
            d[i]=1
        else:
            d[i]=0
    for i in range(1,n+1):
        if i==1 and d[i]==0:
            if d[i+1]==2:
                d[i+1]-=1
                d[i]=1
            continue
        if i==n and d[i]==0:
            if d[i-1]==2:
                d[i-1]=1
                d[i]=1
            continue
        if d[i]==0:
            if d[i-1]==2:
                d[i-1]-=1
                d[i]=1
            elif d[i+1]==2:
                d[i+1]-=1
                d[i]=1
            
        #print(d)
    #print(d)
    for i in range(1,n+1):
        if d[i]>0:
            answer+=1
            #print(d[i])
    return answer