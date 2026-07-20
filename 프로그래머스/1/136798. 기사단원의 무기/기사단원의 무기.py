def solution(number, limit, power):
    answer = 0
    n = [0]*(number+1)
    for i in range(1,number+1):
        for j in range(i,number+1,i):
            n[j]+=1
        if n[i]>limit:
            n[i]=power
    #print(n)
    answer = sum(n)
    return answer