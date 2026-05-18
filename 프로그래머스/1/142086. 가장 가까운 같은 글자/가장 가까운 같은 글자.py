def solution(s):
    answer = []
    d={}
    for i in range(len(s)):
        if not s[i] in d:
            d[s[i]]=i
            answer.append(-1)
        else:
            answer.append(i-d[s[i]])
            d[s[i]]=i
        #print(d)
            
    return answer