from collections import deque
def solution(numbers, target):
    answer = 0
    s = numbers[0]
    q = deque([s, -s])
    for i in range(1,len(numbers)):
        l = len(q)
        for _ in range(l):
            n = q.popleft()
            
            q.append(n+numbers[i])
            q.append(n-numbers[i])
        #print(q)
    answer = q.count(target)
                
    return answer