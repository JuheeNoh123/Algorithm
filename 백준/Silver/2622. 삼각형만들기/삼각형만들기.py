a = int(input())
cnt = 0

for x in range(1, a):
    # y의 최소값
    y_min = max(x, (a // 2 - x + 1))
    
    # y의 최대값
    y_max = (a - x) // 2
    
    if y_min > y_max:
        continue
    
    cnt += (y_max - y_min + 1)

print(cnt)