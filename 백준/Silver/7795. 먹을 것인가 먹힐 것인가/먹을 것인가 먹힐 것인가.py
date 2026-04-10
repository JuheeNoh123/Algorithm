t = int(input())

def bSearch(k, s,e, L):
    
    if s>e:
        return s
    m = (s+e)//2
    #print(s,e,m)
    if L[m]<k:
        return bSearch(k,m+1,e,L)
    else:
        return bSearch(k,s,m-1,L)
    
    
for _ in range(t):
    a,b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()
    s = 0
    e = len(B)-1 
    cnt = 0
    for j in A:
        #print(j)
        c = bSearch(j, s, e, B)
        #print('c', c)
        cnt += c
    print(cnt)