def solution(n):
    cnt = 0
    for i in range(1, n + 1):
        cnt += i
    answer = [0] * cnt

    answer[0] = 1
    index = 0
    num = 2
    gap1 = 1
    for i in range(n - 1):
        index += gap1
        answer[index] = num
        num += 1
        gap1 += 1

    turn = 2
    gap1_s = 2
    gap2_s = n
    gap2 = n
    n -= 1
    gap2_k = 1
    while n > 0:

        if turn == 2:
            for i in range(n):
                index += 1
                answer[index] = num
                num += 1
            n -= 1
            turn += 1
            continue
        # 대각선 왼쪽 위로 올라가는거
        if turn % 3 == 0:
            gap2 = gap2_s
            for i in range(n):
                index -= gap2
                answer[index] = num
                gap2 -= 1
                num += 1
            gap2_s -= 1
            # gap2_k *= 2
        # 대각선 왼쪽아래로 내려가는거
        elif turn % 3 == 1:
            gap1 = gap1_s
            for i in range(n):
                index += gap1
                answer[index] = num
                gap1 += 1
                num += 1
            gap1_s += 2
        # 오른쪽으로 이동
        else:
            for i in range(n):
                index += 1
                answer[index] = num
                num += 1
        turn += 1
        n -= 1
        # print(answer)
    return answer


