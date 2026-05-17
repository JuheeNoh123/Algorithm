def solution(nums):
    answer = 0
    s_nums = set(nums)
    if len(s_nums)<len(nums)//2:
        answer= len(s_nums)
    else:
        answer = len(nums)//2
    return answer