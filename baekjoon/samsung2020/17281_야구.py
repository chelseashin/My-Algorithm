import sys
sys.stdin = open("17281_input.txt")
input = sys.stdin.readline

# Brute Force, 구현
# 이닝별로 아웃카운트, 타자순서 관리(다음 이닝에 첫 타자 인덱스 유지)
# 점수 먼저 더해주고 선수 다음 베이스로 옮기기(순서 바꾸면 X)
# 변수별 초기화 위치 신경쓰기!
# 실수 금지!!!!

def baseball(order):
    global MAX, innings
    score = 0
    hitter_idx = 0
    for inning in innings:
        b1, b2, b3 = 0, 0, 0
        outcount = 0
        while outcount < 3:
            if inning[order[hitter_idx]] == 0:
                outcount += 1
            elif inning[order[hitter_idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif inning[order[hitter_idx]] == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif inning[order[hitter_idx]] == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            elif inning[order[hitter_idx]] == 4:
                score += (1 + b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 0
            hitter_idx = (hitter_idx + 1) % 9
    MAX = max(MAX, score)
    return

def perm(depth):
    if depth == 9:
        # print(order)
        baseball(order)
        return
    for i in range(9):
        if visited[i]:
            continue
        order[i] = depth
        visited[i] = 1
        perm(depth+1)
        visited[i] = 0
        order[i] = 0

N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]
# print(innings)
MAX = 0
order = [0] * 9
visited = [0] * 9
visited[3] = 1
perm(1)
print(MAX)