def solution(X, Y):
    answer = ''
    a = [0,0,0,0,0,0,0,0,0,0]
    b = [0,0,0,0,0,0,0,0,0,0]
    
    for i in X:
        value = int(i)
        a[value] += 1
    for i in Y:
        value = int(i)
        b[value] += 1
    
    for i in range(9,-1,-1):
        value = str(i)*min(a[i],b[i])
        answer += value
    if len(answer)==0:
        return '-1'
    if answer[0]=='0':
        return '0'
    return answer