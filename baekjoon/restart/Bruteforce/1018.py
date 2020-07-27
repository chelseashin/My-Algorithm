import sys
sys.stdin = open('1018_input.txt')

# 성공코드
def solution(r, c):
    global MIN, cnt
    check_color = ['B', 'W']
    for color in range(2):
        cnt = 0
        for nr in range(r, r+8):
            for nc  in range(c, c+8):
                if chess[nr][nc] != check_color[color%2]:
                    cnt += 1
                color += 1
            color += 1
        if MIN > cnt:
            MIN = cnt

N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]
MIN = float('inf')

for i in range(N-7):
    for j in range(M-7):
        solution(i, j)

print(MIN)