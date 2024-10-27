A, B, V = map(int,input().split())
cnt = (V-B)//(A-B)
if (V-B)%(A-B)==0:
      print(cnt)
else:
      print(cnt+1)
      
# A*cnt - B(cnt-1) >= V
# (A-B) * cnt >= V - B