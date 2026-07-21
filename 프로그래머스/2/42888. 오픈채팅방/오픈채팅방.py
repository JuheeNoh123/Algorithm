def solution(record):
    answer = []
    res = []
    dic={}
    for i in range(len(record)):
        L = record[i].split()
        if len(L)==3:
            ELC, id, name = L
            dic[id]=name
        else:
            ELC, id = L
        
        if ELC=='Enter':
            res.append([id, 1])
        elif ELC=='Leave':
            res.append([id,0])
        
        
        
    for r in res:
        if r[1]==1:
            answer.append(f'{dic[r[0]]}님이 들어왔습니다.')
        else:
            answer.append(f'{dic[r[0]]}님이 나갔습니다.')
    return answer