import sys
# from collections import deque
input = sys.stdin.readline

s = input().strip()
pikachu = ['pi','ka','chu']
check="YES"
idx = 0
while idx<len(s):
    if s[idx:idx+3]=='chu':
        #print(s[idx:idx+3])
        idx+=3
    elif s[idx:idx+2]=='pi':
        #print(s[idx:idx+2])
        idx+=2
    elif s[idx:idx+2]=='ka':
        #print(s[idx:idx+2])
        idx+=2
    else:
        check="NO"
        break


print(check)