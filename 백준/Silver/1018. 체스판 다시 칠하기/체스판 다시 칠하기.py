N, M = map(int, input().split())
L = []
cnt = []
for _ in range(N):
      L.append(input())
for a in range(N-7):
      for b in range(M-7):
            w_cnt = 0
            b_cnt = 0
            for i in range(a,a+8):
                  for j in range(b, b+8):
                        if (i+j)%2==0:
                              if L[i][j]=='W':
                                    b_cnt += 1
                              else:
                                    w_cnt+=1
                        else:
                              if L[i][j]=='W':
                                    w_cnt += 1
                              else:
                                    b_cnt+=1
            if w_cnt<b_cnt:
                  cnt.append(w_cnt)
            else:
                  cnt.append(b_cnt)
                  
print(min(cnt))