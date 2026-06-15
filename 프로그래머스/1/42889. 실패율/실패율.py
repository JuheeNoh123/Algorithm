def solution(N, stages):
    answer = []
    l = len(stages)
    for i in range(1,N+1):
        player=0
        clear=0
        for stage in stages:
            if stage==i:
                player +=1
            if stage>=i:
                clear += 1
        if clear==0:
            answer.append([i,0])
        else:
            answer.append([i,player/clear])
    answer.sort(key = lambda x: -x[1])
    answer2 = [x[0] for x in answer]
    return answer2