
n = int(input())
L= list(map(int,input().split()))
L.sort()
#print(L)
def bSearch(s,e,k,arr):
    m = (s+e)//2
    #print(s,e,m)
    if s>e:
        return s
    if k<=arr[m]:
        e = m-1
        return bSearch(s,e,k,arr)
    else:
        s = m+1
        return bSearch(s,e,k,arr)
cnt = 0
for i in range(n-1,-1,-1):
    #print(L[i], 'k: ', L[i]*0.9)
    res = bSearch(0,i-1,L[i]*0.9,L)
    #print(res)
    #print(i-res)
    cnt += (i - res)
print(cnt)