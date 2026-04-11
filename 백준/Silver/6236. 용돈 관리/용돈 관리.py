
n, m = map(int,input().split())
L= []
for i in range(n):
    L.append(int(input()))



def cal(k):
    money = k
    cnt = 1
    for cost in L:
        if money < cost:  #돈이 부족하면 인출
            money=k # 기존에 있던 돈은 다시 넣고, k원만 뽑을 수 있음.
            cnt+=1  #인출 시 횟수 증가
        money -= cost  #하루 사용할 비용 사용.

    if cnt<=m:
        return True
    else:
        return False
    
s = max(L)
e = sum(L)
#이분탐색
def bSearch(l,r):
    m = (r+l)//2
    if l>r:
        return l  #경계값이 정답
    
    if cal(m):
        r = m-1
        return bSearch(l,r)
    else:
        l = m+1
        return bSearch(l,r)

print(bSearch(s,e))
    