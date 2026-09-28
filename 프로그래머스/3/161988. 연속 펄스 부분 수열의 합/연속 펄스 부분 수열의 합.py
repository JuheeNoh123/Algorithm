def solution(sequence):
    answer = -1e9
    dp0, dp1 = 0,0
    for s in sequence:
        n_dp0 = s + max(0, dp1)
        n_dp1 = -s + max(0, dp0)
        dp0, dp1 = n_dp0, n_dp1
        answer = max(answer, dp0, dp1)
    return answer