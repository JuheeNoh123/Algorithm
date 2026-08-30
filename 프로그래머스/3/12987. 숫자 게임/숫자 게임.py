
def solution(A, B):
    answer = 0
    B.sort() 
    A.sort()
    idx=0
    for i in range(len(A)):
        while idx<len(B):
            if B[idx]<=A[i]:
                idx+=1
            else:
                break
        if idx<len(B):
            answer+=1
            idx+=1
            
    return answer