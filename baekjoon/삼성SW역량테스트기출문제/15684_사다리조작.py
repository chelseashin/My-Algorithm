import sys
sys.stdin = open('15684_input.txt')

# 나의 풀이(실패)
# 완전탐색으로 TC 다 맞지만 but 시간 초과
# 아예 다른 접근 방법이 필요하다!

# 시뮬레이션 문제

from itertools import combinations

# 가로 크기, 최대 가로 대각선 수, 세로 크기
N, M, H = map(int, input().split())
info = tuple(list(map(int, input().split())) for _ in range(M))
# print(info)

if M == 0:
    print(0)
    exit()

# 기존의 가로선 제외한 그릴 수 있는 모든 가로선 경우
total = []
for i in range(1, H+1):
    for j in range(1, N):
        if [i, j] not in info:
            total.append([i, j])
# print(total)

ans = -1
for i in range(1, 4):
    for comb in combinations(total, i):
        C = info + comb
        check = 0   # 자기의 번호에 잘 도착했는지 체크
        for start in range(1, N + 1):
            sr, sc = 0, start
            while 1:
                if sr == H:
                    if sc == start:
                        check += 1
                    break
                r = sr + 1
                c = sc
                if [r, c] in C:
                    c = sc + 1
                elif [r, c - 1] in C:
                    c = sc - 1
                sr, sc = r, c

            if check != start:      # 이미 실패하면
                break
        if check == N:
            print(i)
            exit()
print(ans)