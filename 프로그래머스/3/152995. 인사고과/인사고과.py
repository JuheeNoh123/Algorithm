
def solution(scores):
    answer = 0
    t_a, t_b = scores[0][0], scores[0][1]
    
    scores.sort(key = lambda x:(-x[0],x[1]))
    #print(scores)
    m_b=0
    for i in range(len(scores)):
        if scores[i][0]>t_a and scores[i][1]>t_b:
            return -1
        if m_b<=scores[i][1]:
            m_b=scores[i][1]
            if t_a+t_b < scores[i][0]+scores[i][1]:
                answer+=1
                
        
            
    return answer+1