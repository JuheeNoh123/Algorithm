from itertools import permutations


def ee(num):
    if num==1 or num==0:
        return 0
    for i in range(2,num):
        if num%i==0:
            return 0
    return 1
    
    
def solution(numbers):
    answer = 0
    s = set()
    for j in range(1,len(numbers)+1):
        for i in permutations(list(numbers), j):
            n = ''
            for k in i:
                n+=k
            s.add(int(n))
    #print(s)
    for i in s:
        #print(ee(i))
        answer += ee(i)
    
    return answer