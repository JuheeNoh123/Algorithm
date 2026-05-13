def solution(participant, completion):
    answer = ''
    d={}
    for i in participant:
        if d.get(i)==None:
            d[i]=1
        else:
            d[i] +=1
    
    for i in completion:
        d[i]-=1
    for k,v in d.items():
        if v!=0:
            answer=k
            return answer