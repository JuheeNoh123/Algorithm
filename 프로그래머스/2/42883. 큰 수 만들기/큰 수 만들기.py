
def solution(number, k):
    answer = ''
    
    L = [number[0]]
    cnt = 0
    for i in range(1,len(number)):
        while len(L)>0 and int(L[-1])<int(number[i]) and cnt<k:
            L.pop()
            cnt+=1
        L.append(number[i])
        #print(L)
    
    if cnt<k:
        L = L[:len(L)-(k-cnt)]
    answer = answer.join(L)
    return answer