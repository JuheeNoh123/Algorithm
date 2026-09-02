def solution(s):
    answer = ''
    #print(ord('A'), ord('a'))
    
    
    start = 0 #새로 시작하는 단어인가
    for i in range(len(s)):
        if s[i]==' ':
            answer += ' '
            start=i+1
            continue
        if i==start: 
            if ord('a')<=ord(s[start])<=ord('z'):
                answer+=chr(ord(s[start])-32)
            else:
                answer+=s[start]
        else:
            if ord('A') <= ord(s[i])<=ord('Z'):
                answer+=chr(ord(s[i])+32)
            else:
                answer+=s[i]
        
                

    return answer