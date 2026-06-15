from itertools import permutations
def solution(n):
    L = [0]*(n+1)
    L[1] = 1
    if n>=2:
        L[2]=2
    for i in range(3, n+1):
        L[i]=(L[i-1]%1234567)+(L[i-2]%1234567)
    answer = L[n]%1234567
    return answer