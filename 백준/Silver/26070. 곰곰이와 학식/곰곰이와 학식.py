import sys
input = sys.stdin.readline

food = list(map(int, input().split()))
coupon = list(map(int, input().split()))

total = 0

for i in range(3):
    small = min(food[i],coupon[i])
    total+=small
    if food[i]==small:
        food[i]=0
        coupon[i] -= small
    else:
        coupon[i]=0
        food[i] -= small
        
# print(food)
# print(coupon)

for i in range(3):  #치킨, 피자 대상 쿠폰 교환
    if coupon[i] and food[i]:
        if coupon[i]>food[i]:
            total += food[i]
            coupon[i]-=food[i]
            food[i]=0
            
            
        else:
            total+=coupon[i]
            food[i]-=coupon[i]
            coupon[i]=0
            
    # print(total)
    # print(food)
    # print(coupon)
            
    if coupon[i]>=3:
        if i==2:
            i=-1
        #print(i)
        change = coupon[i]//3
        coupon[i+1] +=change
        coupon[i]=coupon[i]%3
        

    # print(total)
    # print(food)
    # print(coupon)

for i in range(2):
    if food[i] and coupon[i]:
        if food[i]>coupon[i]:
            total+=coupon[i]
            food[i]-=coupon[i]
            coupon[i]=0
        else:
            total+=food[i]
            coupon[i]-=food[i]
            food[i]=0
    if coupon[i]>=3:
        #print(i)
        change = coupon[i]//3
        coupon[i+1] +=change
        coupon[i]=coupon[i]%3

print(total)