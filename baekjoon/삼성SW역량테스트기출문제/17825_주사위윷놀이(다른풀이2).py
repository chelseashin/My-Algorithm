import sys
sys.stdin = open('17825_input.txt')
input = sys.stdin.readline

score_board = [
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38],
    [13, 16, 19],   # 10에서 시작
    [22, 24],       # 20에서 시작
    [28, 27, 26],   # 30에서 시작
    [25, 30, 35],   # 25에서 시작
    [40]            # 도착
]

def solve(depth, score):
    global MAX
    if depth == 10:
        MAX = max(MAX, score)
        return

    for i in range(4):
        # 도착지점에 있는 값 제외
        if horse[i] == [5, 1, 0]:
            continue
        # 시작 위치가 같으면 제외
        same_pos = False
        for j in range(i):
            if horse[i] == horse[j]:
                same_pos = True
                break
        if same_pos:
            continue
        # 이동
        x, y, v = horse[i]      # 방향, 인덱스, 점수
        for _ in range(move[depth]):
            y += 1
            if y == len(score_board[x]):
                # 도착
                if x == 0 or x == 4:
                    y = 0
                    x = 5
                elif x < 4:
                    y = 0
                    x = 4
                else:
                    v = 0      # 도착
                    break
            v = score_board[x][y]
        # 마지막 칸이 파란색 화살표인 경우
        if x == 0:
            if v == 10:
                x, y = 1, -1
            elif v == 20:
                x, y = 2, -1
            elif v == 30:
                x, y = 3, -1

        # 이동 마치는 칸에 다른 값 존재하지 않으면 이동 가능
        # 단, 도착지점일 경우 중복 가능
        can_move = True
        if v != 0:
            for j in range(4):
                if i == j:
                    continue
                if horse[j] == [x, y, v]:
                    can_move = False
                    break
        if can_move:
            x, y, v, horse[i] = horse[i][0], horse[i][1], horse[i][2], [x, y, v]

            solve(depth+1, score+horse[i][2])
            horse[i] = [x, y, v]

# main
move = list(map(int, input().split()))
MAX = 0
horse = [[0, 0, 0] for _ in range(4)]

solve(0, 0)
print(MAX)