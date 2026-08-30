def solution(n, info):
    best_arr = None
    best_diff = 0
    def dfs(idx, remaining, ryan):
        nonlocal best_diff, best_arr
        if idx==10:
            ryan = ryan[:] #얕은 복사 후 사용 (원본 직접 안건드림)
            ryan[10] += remaining #남은 화살 0점에 몰아넣기
        
            apeach_score = 0
            ryan_score = 0
            for i in range(11):
                score = 10-i
                if info[i] == 0 and ryan[i] == 0:
                    continue
                if ryan[i] > info[i]:
                    ryan_score += score
                else:
                    apeach_score += score

            diff = ryan_score - apeach_score
            if diff> 0 and diff>=best_diff: #점수차가 큰걸 선택
                #점수차가 같은 경우 낮은 점수 많이 맞힌 배열 선택
                if diff>best_diff or best_arr is None or better(ryan, best_arr):
                    best_arr=ryan
                    best_diff = diff
            return
        
        #1) 이 점수 포기
        dfs(idx+1, remaining, ryan)
        
        #2) 이 점수 뺏기
        need = info[idx]+1
        if remaining>=need: #뺏을 수 있으면
            ryan[idx]+=need
            dfs(idx+1, remaining-need, ryan)
            ryan[idx]-=need #다시 되돌려서 다음 탐색에서 새롭게 시작
            
            
    def better(a,b): #낮은 점수 많이 맞힌 배열 리턴
        for i in range(10, -1, -1):
            if a[i] != b[i]:
                return a[i]>b[i]
        return False
    
    dfs(0,n,[0]*11)
    return best_arr if best_arr else [-1]