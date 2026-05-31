from collections import deque
def solution(priorities, location):
    answer = 0
    l = []
    d = deque()
    ans=[]
    for i in range(len(priorities)):
        d.append([i,priorities[i]])
    while len(d):
        #print(d)
        m = max(d, key=lambda x:x[1])[1]
        a = d.popleft()
        if a[1]!=m:
            d.append(a)
        else:
            ans.append(a[0])
    answer=ans.index(location)+1
    return answer