def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        Q = i//n#몫
        P = i%n #나머지
        #print(Q,P)
        if Q==0:
            answer.append(P+1)
        elif Q==n-1:
            answer.append(n)
        else:
            if P<=Q: answer.append(Q+1)
            else: answer.append(P+1)
        #print(answer)
    
    
            

    return answer