def solution(arr):
    nums = [int(x) for x in arr[::2]]
    ops = arr[1::2]
    n = len(nums)

    dp_max = [[0] * n for _ in range(n)]
    dp_min = [[0] * n for _ in range(n)]

    for i in range(n):
        dp_max[i][i] = dp_min[i][i] = nums[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            mx, mn = float('-inf'), float('inf')
            for k in range(i, j):  # i~k 구간과 k+1~j 구간을 합침
                op = ops[k]
                if op == '+':
                    mx = max(mx, dp_max[i][k] + dp_max[k+1][j])
                    mn = min(mn, dp_min[i][k] + dp_min[k+1][j])
                else:  # '-'
                    mx = max(mx, dp_max[i][k] - dp_min[k+1][j])
                    mn = min(mn, dp_min[i][k] - dp_max[k+1][j])
            dp_max[i][j] = mx
            dp_min[i][j] = mn

    return dp_max[0][n-1]