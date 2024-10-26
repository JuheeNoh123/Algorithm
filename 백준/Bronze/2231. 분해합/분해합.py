N = int(input())
for i in range(1,N+1):
      sum = i
      s = str(i)
      for j in s:
            sum += int(j)
      if sum==N:
            sum=i
            break
      else:
            sum=0
print(sum)