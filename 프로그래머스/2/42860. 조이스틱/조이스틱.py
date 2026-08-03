def solution(name):
    answer = 0
    n = len(name)
    for i in range(n):
        
        fromA = ord(name[i])-ord('A')
        fromZ = ord('Z')-ord(name[i])+1
        answer += min(fromA, fromZ)
    
    min_move = n-1
    for i in range(n):
        next_i = i+1
        while next_i<len(name) and name[next_i]=='A':
            next_i+=1
        
        m_right = i*2+n-next_i
        m_left = (n-next_i)*2+i
        min_move = min(min_move, m_right, m_left)
        
    answer+=min_move
    return answer