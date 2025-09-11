import sys
input = sys.stdin.readline

time = input().strip()
m,s = map(int, time.split(':'))
flag = False #조리 여부
total = m*60 + s
if total ==30:
    print(1)
else:
    # 10s, 1m, 10m, 30s(start)
    cnt = 0

    cnt+=total//600
    #print(total, cnt)
    total = total%600
    cnt += total//60
    #print(total, cnt)
    total = total%60
    #print(total, cnt)
    if total>=30:
        cnt+=1
        total -=30
        cnt += total//10
    else:
        cnt+=1 #시작
        cnt += total//10
    
    print(cnt)
