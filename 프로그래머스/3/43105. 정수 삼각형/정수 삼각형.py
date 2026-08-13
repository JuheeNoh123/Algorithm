import copy
def solution(triangle):
    answer = 0
    new_t = copy.deepcopy(triangle)
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            #print(new_t[i+1][j], triangle[i+1][j],new_t[i][j])
            new_t[i+1][j] = max(new_t[i+1][j], triangle[i+1][j]+new_t[i][j])
            #print(new_t[i+1][j+1], triangle[i+1][j+1],new_t[i][j])
            new_t[i+1][j+1]= max(new_t[i+1][j+1], triangle[i+1][j+1]+new_t[i][j])
        #print(new_t)
    return max(new_t[-1])