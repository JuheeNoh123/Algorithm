def solution(n, words):
    answer = []
    num = 1
    turn = 1
    check = {words[0]}
    for w in range(1,len(words)):
        num+=1
        
        if num>n:
            num=1
            turn +=1
        #print(num, turn)
        if words[w-1][-1]!=words[w][0]:
            answer = [num,turn]
            break
        
        if len(check & {words[w]}) >0 :
            answer = [num,turn]
            break
        check.add(words[w])
        
    if len(answer)==0:
        answer = [0,0]
    return answer