import sys
sys.stdin = open('06_input.txt')

from itertools import permutations

def play(lineup):
    score = 0
    hitter_idx = 0
    for inning in innings:
        out, b1, b2, b3 = 0, 0, 0, 0
        while out <= 2:
            if inning[lineup[hitter_idx]] == 0:
                out += 1
            elif inning[lineup[hitter_idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif inning[lineup[hitter_idx]] == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif inning[lineup[hitter_idx]] == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            elif inning[lineup[hitter_idx]] == 4:
                score += (b1 + b2 + b3 + 1)
                b1, b2, b3 = 0, 0, 0
            hitter_idx = (hitter_idx + 1) % 9
    return score

N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]

max_score = 0
for order in list(permutations(range(1, 9))):
    lineup = list(order[0:3]) + [0] + list(order[3:])
    # print(lineup)
    max_score = max(max_score, play(lineup))

print(max_score)