import sys
sys.stdin = open('2105_input.txt')

def my_calc():
    for length in range(N - 1, 1, -1):
        for i in range(1, length):
            j = length - i
            for r in range(i, N - j):
                for c in range(N - i - j):
                    # 출발
                    visited = [False] * 101
                    y, x = r, c
                    for d in range(4):  # 방향 전환
                        n = j if d % 2 else i
                        for _ in range(n):  # 직진
                            y, x = y + dy[d], x + dx[d]
                            if not visited[MAP[y][x]]:
                                visited[MAP[y][x]] = True
                            else:  # 중복이면 다음 출발로
                                break
                        else:
                            continue
                        break
                    else:  # 한바퀴 완주하면
                        return length * 2
    return -1


dx = [1, 1, -1, -1]
dy = [-1, 1, 1, -1]

T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    print('#{} {}'.format(test_case, my_calc()))