import sys
input = sys.stdin.readline

N, K = map(int, input().split())

L = list(map(int, input().split()))

end = 0
cnt=0
odd = 0
m=0

        

for start in range(N):
    while (end<N and odd<=K):
        if L[end]%2==0:
            cnt+=1
        else:
            odd+=1
        #print(cnt, odd) 
        end+=1  
    m = max(cnt, m)
    
    #start 지점이 바뀌므로 하나씩 삭제
    if L[start] % 2:
        odd -= 1
    else:
        cnt -= 1
print(m)