def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        c = arr1[i]|arr2[i]
        a= bin(c)[2:]
        if len(a)<n:
            a='0'*(n-len(a))+a
        s=''
        for j in a:
            if j=='1':
                s+='#'
            else:
                s+=' '
        answer.append(s)
        
    return answer