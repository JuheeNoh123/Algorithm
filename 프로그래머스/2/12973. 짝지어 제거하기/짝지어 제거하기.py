def solution(s):
    answer = 0
    stack = []
    for i in s:
        if len(stack)!=0 and stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack)==0:
        answer=1
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
   # print('Hello Python')

    return answer