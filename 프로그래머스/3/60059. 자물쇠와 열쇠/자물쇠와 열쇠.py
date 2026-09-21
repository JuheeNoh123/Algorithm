def rotate_90(a):
    n = len(a)
    m= len(a[0])
    res = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            res[j][n-i-1]=a[i][j]
    return res

def check(new_lock):
    lock_len = len(new_lock)//3
    for i in range(lock_len, lock_len*2):
        for j in range(lock_len, lock_len*2):
            if new_lock[i][j] !=1:
                return False
    return True

def solution(key, lock):
    
    n = len(lock)
    m = len(key)
    
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    #print(new_lock)
    
    #4가지 방향 확인
    for r in range(4):
        key = rotate_90(key) #열쇠 회전
        #print(key)
        for x in range(n*2):
            for y in range(n*2):
                #자물쇠에 열쇠 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]+=key[i][j]
                #print(new_lock)
                #새로운 자물쇠에 열쇠가 정확히 들어맞는가?
                if check(new_lock):
                    return True
                #자물쇠에서 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
                
    return False