L = int(input())
s = input()
X=[]
for i in s:
      X.append(ord(i)-96)
sum = 0
for i in range(L):
      sum += X[i]*(31**i)
print(sum%1234567891)