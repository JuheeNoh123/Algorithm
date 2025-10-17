import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s =[]
    for i in range(4):
        x,y = map(int,input().split())
        s.append((x,y))
    s.sort()
    flag=0
    x1x2 = (s[0][0]-s[1][0])**2 + (s[0][1]-s[1][1])**2
    x3x4 = (s[2][0]-s[3][0])**2 + (s[2][1]-s[3][1])**2
    x1x3 = (s[0][0]-s[2][0])**2 + (s[0][1]-s[2][1])**2
    x2x4 = (s[1][0]-s[3][0])**2 + (s[1][1]-s[3][1])**2
    x2x3 = (s[1][0]-s[2][0])**2 + (s[1][1]-s[2][1])**2 #대각선 길이
    x1x4 = (s[0][0]-s[3][0])**2 + (s[0][1]-s[3][1])**2 #대각선 길이
    if x1x2==x3x4 and x2x4==x1x3 and x1x2 == x2x4 :#모든 변의 길이 같은지 검사
        if x2x3 == x1x4:
            flag=1
    if flag:
        print(1)
    else:
        print(0)      