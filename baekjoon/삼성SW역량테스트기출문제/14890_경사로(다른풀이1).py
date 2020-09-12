import sys
sys.stdin = open('14890_input.txt')

# 참고 링크
# https://calmlife.tistory.com/34

def solve(r, c, dr, dc):
    cnt = 1
    for _ in range(N-1):
        nr, nc = r + dr, c + dc
        diff = A[nr][nc] - A[r][c]
        if abs(diff) > 1:
            return 0
        if diff == 1:     # 이전 높이보다 높으면
            if cnt >= L:  # 경사로 건설 후 초기화
                cnt = 0
            else:
                return 0    # 건설 못하면
        if diff == -1:      # 이전 높이보다 낮으면
            if cnt >= 0:
                cnt = -L    # 카운트 음수로 만들어줌
            else:
                return 0
        cnt += 1
        r, c = nr, nc
    if cnt >= 0:
        return 1
    return 0

# main
N, L = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    ans += solve(0, i, 1, 0)
    ans += solve(i, 0, 0, 1)
print(ans)