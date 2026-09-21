def solution(picks, minerals):
    groups = [minerals[i:i+5] for i in range(0, len(minerals), 5)]
    total_picks = sum(picks)

    # 1. 순서대로 앞에서 total_picks개만 "실제로 채굴되는 그룹"으로 확정
    groups = groups[:total_picks]

    # 2. 이 그룹들 안에서만 다이아/철 개수로 정렬해서 곡괭이 배정 순서를 정함
    groups.sort(key=lambda g: (-g.count('diamond'), -g.count('iron')))

    pick_order = ['diamond']*picks[0] + ['iron']*picks[1] + ['stone']*picks[2]
    cost_table = {
        'diamond': {'diamond': 1, 'iron': 1, 'stone': 1},
        'iron':    {'diamond': 5, 'iron': 1, 'stone': 1},
        'stone':   {'diamond': 25, 'iron': 5, 'stone': 1},
    }

    answer = 0
    for pick, group in zip(pick_order, groups):
        for m in group:
            answer += cost_table[pick][m]
    return answer