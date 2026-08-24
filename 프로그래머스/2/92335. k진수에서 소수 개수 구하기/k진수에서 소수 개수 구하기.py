def k_jinsoo(n,k):
    res = ''
    while n>1:
        
        res = str(n%k)+res
        n = n//k
        #print(res)
    res=str(n)+res
    return int(res)
def check_sosoo(p):
    if p==1:
        return False
    if p==2:
        return True
    for i in range(2,int(p**(0.5))+1):
        if p%i==0:
            return False
    return True
def solution(n, k):
    answer = 0
    s = str(k_jinsoo(n,k))
    #print(s)
    p_list = s.split('0')
    for p in p_list:
        if p=='':
            continue
        if check_sosoo(int(p)):
            answer += 1
    return answer