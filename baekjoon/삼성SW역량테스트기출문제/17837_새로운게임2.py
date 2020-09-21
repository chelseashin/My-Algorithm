import sys
sys.stdin = open('17837_input.txt')
input = sys.stdin.readline

# 시뮬레이션 문제
# 로직 어렵지 않으니 포기하지 말고 생각한 대로 구현해보자

# 우, 좌, 상, 하
dr = (0, 0, -1, 1)
dc = (1, -1, 0, 0)

# 방향 전환
rev = (1, 0, 3, 2)

def solve():
    turn = 0
    while True:
        turn += 1
        if turn > 1000:
            print(-1)
            return
        for num in range(1, K+1):
            r, c, d = horse[num]
            nr = r + dr[d]
            nc = c + dc[d]
            # 이동하려는 칸이 맵 벗어나거나 파란색 칸인 경우
            if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == blue:
                d = rev[d]
                nr = r + dr[d]
                nc = c + dc[d]
                # 맵 벗어나거나 파란색 칸인 경우
                if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == blue:
                    horse[num][2] = d  # 방향만 바뀜
                    continue
            # 이동하려는 칸이 흰색인 경우
            if board[nr][nc] == white:
                left = B[(r, c)][:B[(r, c)].index(num)]
                right = B[(r, c)][B[(r, c)].index(num):]
                B[(r, c)] = left
                B[(nr, nc)].extend(right)
                if len(B[(nr, nc)]) >= 4:
                    print(turn)
                    return
                for i in right:         # 좌표 갱신
                    horse[i][0] = nr
                    horse[i][1] = nc
                horse[num][2] = d
            # 이동하려는 칸이 빨간색인 경우
            elif board[nr][nc] == red:
                left = B[(r, c)][:B[(r, c)].index(num)]
                right = B[(r, c)][B[(r, c)].index(num):]
                B[(r, c)] = left
                B[(nr, nc)].extend(reversed(right))
                if len(B[(nr, nc)]) >= 4:
                    print(turn)
                    return
                for i in right:
                    horse[i][0] = nr
                    horse[i][1] = nc
                horse[num][2] = d

# main
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# K개 말의 [현재 위치와 방향]을 표현
horse = {}
# 보드에 [말이 놓여진 상태]를 표현
B = {(i, j): [] for j in range(N) for i in range(N)}

for i in range(1, K+1):
    r, c, d = map(int, input().split())
    horse[i] = [r-1, c-1, d-1]
    B[(r-1, c-1)].append(i)

white = 0
red = 1
blue = 2
# print(horse)
# print(B)
solve()