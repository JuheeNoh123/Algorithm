def solution(want, number, discount):
    answer = 0    
    w_l=len(want)
    
    l = len(discount)
    for i in range(0,l):
        a = discount[i:i+10]
        #print(a)
        b = {}
        for i in range(w_l):
            b[want[i]]=number[i]
        flag=True
        for j in range(len(a)):
            if b.get(a[j])!=None:
                b[a[j]]-=1
        #print(b)
        for k in b:
            if b[k]>0:
                flag =False
        #print(flag)
        if flag:
            answer+=1
        
    return answer