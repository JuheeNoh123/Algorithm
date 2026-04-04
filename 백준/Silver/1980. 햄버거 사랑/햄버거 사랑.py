n, m , t = map(int, input().split())

a = t//n
cnt = a
cola= t
for i in range(a, -1, -1):
    tower_cnt = i
    bul_cnt = (t - i*n) // m
    c = t- tower_cnt*n - bul_cnt*m
    
    #print(tower_cnt, bul_cnt, c)
    if c>=0 and c < cola:
        cnt = tower_cnt+bul_cnt
        cola = c
    elif c==cola:
        if tower_cnt+bul_cnt > cnt:
            cnt = tower_cnt+bul_cnt
    
print(cnt, cola)