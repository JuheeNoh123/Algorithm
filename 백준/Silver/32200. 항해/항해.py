import sys
input = sys.stdin.readline
n,x,y = map(int, input().split())
bread = list(map(int, input().split()))

cnt = 0
waste = 0

for i in bread:
    day = i//x  #내가 먹을 수 있는 최대 끼니수
    #print(day)
    can = day*y #내가 먹을 수 있는 최대 샌드위치 길이
    cnt += day
    if can<=i:
        waste += i-can
    
        
    
print(cnt)
print(waste)
  