
def solution(message, spoiler_ranges):
    answer = 0
    message+=' '
    info = []
    s=''
    n=[]
    
    for i in range(len(message)):
        if message[i]==' ':
            #n.pop()
            info.append([s,n])
            s=''
            n=[]
            continue
        s+=message[i]
        n.append(i)
    #print(info)
    sp=[]
    for i in range(len(spoiler_ranges)):
        A = set([j for j in range(spoiler_ranges[i][0],spoiler_ranges[i][1]+1)])
        #print(A)
        #flag=0
        for k in range(len(info)):
            B = set(info[k][1])
            #print(B)
            if len(A&B)>=1:
                #info[k][2] = 1
                sp.append(info[k])
    
    for i in range(len(info)):
        for j in range(len(sp)):
            if info[i][0]==sp[j][0] and info[i][1]==sp[j][1]:
                info[i]=[-1,-1]
                break
    #print(info)     
    
    
    for i in range(len(sp)):
        idx=0
        flag=0
        while idx<len(info):
            if info[idx][0]==-1:
                idx+=1
                continue
            if sp[i][0]==info[idx][0]:
                flag=1
                break
            idx+=1
        info.append(sp[i])
        if flag==0:
            answer+=1
    return answer