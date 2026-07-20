def solution(topping):
    answer = 0

    cut={}
    left={}
    for i in range(len(topping)):
        if left.get(topping[i])==None:
            left[topping[i]]=1
        else:
            left[topping[i]]+=1
    #print(left)
    for i in range(len(topping)):
        if cut.get(topping[i])==None:
            cut[topping[i]]=1
        else:
            cut[topping[i]]+=1
        if left.get(topping[i])!=None :
            #print("left[topping[i]]", topping[i])
            if left[topping[i]]>0:
                left[topping[i]]-=1
                if left[topping[i]]==0:
                    del left[topping[i]]
        #print( cut, left)
        if len(cut)==len(left):
            answer+=1
    return answer