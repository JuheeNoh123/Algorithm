from collections import deque
def solution(s):
    answer = True
    d = deque()
    for i in s:
        if i==')':
            if not len(d)==0 and d[-1]=='(':
                d.pop()
            else:
                d.append(')')
        else:
            d.append('(')
        #print(d)
    if len(d)!=0:
        answer=False
            

    return answer