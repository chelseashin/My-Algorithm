import sys
sys.stdin = open('17135_input.txt')

from collections import deque

# 좌, 우, 상
dr = (0, 0, -1)
dc = (-1, 1, 0)

# 적이 더 이상 없는지 확인
# def check_empty():
#     for i in range(N):
#         for j in range(M):
#             if field[i][j]:
#                 return False
#     return True

def enemy_down(field):
    # global field
    # 방법 1 - 간편
    field.pop(N-1)
    field.insert(0, [0] * M)
    # 방법 2
    # for r in range(N-1):
    #     for c in range(M):
    #         if field[N-2-r][c]:
    #             field[N-2-r][c] = 0
    #             field[N-1-r][c] = 1
    #         else:
    #             field[N-1-r][c] = 0


# 공격 가능 거리 내에 있는 적 제거(BFS)
def attack_enemy(pos):
    global field, D, temp
    Q = deque()
    for i in range(M):
        if pos[i]:
            Q.append((N, i))
    print(Q)
    # while Q:
    #     r, c = Q.popleft()
    #     for i in range(3):
    #         nr = r + dr[i]
    #         nc = c + dc[i]
    #         if not (0 <= nr < N and 0 <= nc < M):
    #             continue
    # enemy_down(field)


# 궁수 3명의 위치 정하기
def dfs(depth, k):
    global M, max_attack
    if depth == 3:
        field = raw
        field.append(archer_position)
        print(field)
        temp = 0
        attack_enemy(archer_position)
        if max_attack < temp:
            max_attack = temp
        # 궁수 없애기
        field.pop()
        return
    for i in range(k, M):
        if archer_position[i]:
            continue
        archer_position[i] = 2
        dfs(depth+1, i+1)
        archer_position[i] = 0

# 맵의 세로크기, 가로크기, 최대공격거리
N, M, D = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]

# 최대 공격 가능한 적의 수
max_attack = 0
archer_position = [0] * M
dfs(0, 0)
# print(raw)
# print(max_attack)