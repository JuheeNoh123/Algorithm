import sys
input = sys.stdin.readline
S = 0
M = int(input())
for _ in range(M):
    rule = input()
    if 'add' in rule:
        x = int(rule[4:])-1
        S |= 1<<x
    elif 'remove' in rule:
        x = int(rule[7:])-1
        S &= ~(1<<x)
    elif 'check' in rule:
        x = int(rule[6:])-1
        if S&(1<<x):
            print(1)
        else:
            print(0)
    elif 'toggle' in rule:
        x = int(rule[7:])-1
        if S&(1<<x):
            S ^= 1<<x
        else:
            S |= 1<<x
    elif 'all' in rule:
        S = (1<<20)-1
    elif 'empty' in rule:
        S = 0
    #print(bin(S)[2:])