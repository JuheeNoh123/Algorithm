def solution(lottos, win_nums):
    order = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    answer = []
    cnt_0 = lottos.count(0)
    print(cnt_0)
    A = len(set(lottos) & set(win_nums))
    answer=[order[A+cnt_0], order[A]]
    return answer