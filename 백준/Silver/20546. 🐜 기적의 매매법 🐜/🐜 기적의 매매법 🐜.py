import sys
from collections import deque

input = sys.stdin.readline

def bnp(L,money):
    amount = 0
    for i in range(14):
        if L[i]<=money:
            amount += money//L[i]
            money = money%L[i]
    return money+amount*L[-1]


def timing(L,money):
    d_cnt,i_cnt,amount,total = 0,0,0,0
    for i in range(1,14):
        if L[i-1]>L[i]:
            d_cnt +=1
        else:
            d_cnt=0
        if L[i-1]<L[i]:
            i_cnt += 1
        else:
            i_cnt=0
        if d_cnt>=3 and money>=L[i]:
            amount += money// L[i]
            #print(i+1,'일')
            money = money%L[i]
        elif i_cnt>=3 and amount != 0:
            #print(i+1,'일')
            total += amount * L[i]
            amount = 0
        
        #print(amount, total)
    total += amount*L[-1]
    return total+money

m = int(input())
L = list(map(int, input().split()))
sm = timing(L,m)
jh = bnp(L,m)

if sm>jh:
    print("TIMING")
elif sm<jh:
    print("BNP")
else:
    print("SAMESAME")