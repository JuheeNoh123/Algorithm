def solution(array, commands):
    result = []
    for i in commands:
        ans = array[i[0]-1:i[1]]
        ans.sort()
        result.append(ans[i[2]-1])
    print(result)
    return result 