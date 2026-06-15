def solution(n, w, num):
    answer = 0
    L= [[0]*w for _ in range(100//w+1)]
    i=1
    cnt=0
    col=0
    row=0
    while i<=n:
        if cnt%2==0:
            for b in range(w):
                if i>n:
                    break
                if i==num:
                    col = b
                    row = cnt
                L[cnt][b]=i
                i+=1
        else:
            for b in range(w-1, -1, -1):
                if i>n:
                    break
                if i==num:
                    col = b
                    row = cnt
                L[cnt][b]=i
                i+=1
        cnt +=1
    #print(col, row)
    for i in range(100//w+1):
        if L[i][col]>0:
            answer+=1
    answer -= row
    
    return answer