from itertools import combinations
def solution(clothes):
    answer = 1
    d={}
    for i in clothes:
        if i[1] in d:
            d[i[1]]+=1
        else:
            d[i[1]]=1
    #print(d)
    
    for i in d.values():
        answer *= i+1
    answer-=1
        
    return answer