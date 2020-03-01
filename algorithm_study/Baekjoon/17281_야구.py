import sys
sys.stdin = open("17281_input.txt")

from itertools import permutations

def game(order):
    global inning
    hitter_idx = 0
    score = 0
    for each_inning in inning:
        outcount = 0
        b1, b2, b3 = 0, 0, 0
        while outcount < 3:
            if each_inning[order[hitter_idx]] == 0:
                outcount += 1
            elif each_inning[order[hitter_idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif each_inning[order[hitter_idx]] == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif each_inning[order[hitter_idx]] == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            elif each_inning[order[hitter_idx]] == 4:
                score += (b1 + b2 + b3 + 1)
                b1, b2, b3 = 0, 0, 0

            hitter_idx = (hitter_idx + 1) % 9
    return score

def perm(depth):
    global result, total_count, cnt, MAX
    if depth == 9:
        MAX = max(MAX, game(order))
        # print(order)
        return MAX
    if depth == 3:
        order.append(0)
        perm(depth + 1)
        order.pop()
    else:
        for i in range(1, 9):
            if visited[i]:
                continue
            visited[i] = 1
            order.append(i)
            perm(depth+1)
            order.pop()
            visited[i] = 0

N = int(input())
inning = [list(map(int, input().split())) for _ in range(N)]
MAX = float('-inf')

# 방법 1
visited = [0] * 9
order = []
# perm(0)

# 방법 2
for line_up in permutations(range(1, 9), 8):
    line_up = list(line_up[:3]) + [0] + list(line_up[3:])
    MAX = max(MAX, game(line_up))

print(MAX)
