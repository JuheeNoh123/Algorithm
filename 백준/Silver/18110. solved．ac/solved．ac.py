import sys
def my_round(num):
      if num%1>=0.5:
            return int(num)+1
      else:
            return int(num)


N = int(sys.stdin.readline().strip())

if N==0:
      print(0)

else:
      L = [int(sys.stdin.readline().strip()) for _ in range(N)]
      L.sort()
      
      p15 = my_round(N*0.15)
      #print(p15)
      trimmed_list = L[p15:N - p15]
      #print(trimmed_list)
      
     
      avg = sum(trimmed_list)/len(trimmed_list)
      print(my_round(avg))
