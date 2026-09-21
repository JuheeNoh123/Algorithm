def solution(sticker):
    answer = 0
    if len(sticker)==1:
        return sticker[0]
    dp1 = [0]+sticker[:-1]
    #print(dp1)
    for i in range(2, len(sticker)):
        dp1[i] = max(dp1[i-1], dp1[i]+dp1[i-2])
        #print(dp1)
    dp2 = [0]+sticker[1:]
    #print(dp2)
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i-1], dp2[i]+dp2[i-2])
        #print(dp2)
    return max(dp2[-1],dp1[-1])