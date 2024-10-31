import sys
input = sys.stdin.readline
K,N = map(int, input().split())
L = [int(input()) for _ in range(K)]
#K, N = 4, 11
#L = [802, 743, 457, 539]
start = 1
end = max(L)
t = end  
while start<=end:
      #print("start", start, "end", end)
      #print("t", t)
      cnt = 0
      for i in range(K):
            cnt += L[i]//t
            #print("cnt", cnt)
      if cnt < N:
            end = t-1
      else:
            start = t+1

      t = (start+end)//2
      


print(t)
      
      
