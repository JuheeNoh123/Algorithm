def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack = [[0,numbers[0]]]
    for i in range(1,len(numbers)):
        while len(stack)>0 and numbers[i]>stack[-1][1]:
            idx, num = stack.pop()
            answer[idx]=numbers[i]
        stack.append([i,numbers[i]])
    return answer