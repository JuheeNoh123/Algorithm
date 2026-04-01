a =int(input())
cnt = 0
for i in range(a):
    for j in range(i,a):
        k = a-i-j
        if k<j:
            break
        if k<i+j:
            cnt += 1
print(cnt)