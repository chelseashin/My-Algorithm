from sys import stdin
input = stdin.readline

# 8방향
dr = (-1, 1, 0, 0, -1, 1, -1, 1)
dc = (0, 0, -1, 1, -1, 1, 1, -1)

def solve():
    for r in range(10):
        for c in range(10):
            if A[r][c] == ".":      # 빈 공간 기준일 때 체크해야 함.
                if check(r, c):
                    return 1
    return 0

def check(r, c):
    if go(r, c, [0, 1]):
        return True
    if go(r, c, [2, 3]):
        return True
    if go(r, c, [4, 5]):
        return True
    if go(r, c, [6, 7]):
        return True

def go(r, c, dir):
    totalCnt = 1    # X 갯수 - 빈 공간에 X 놓은 걸로 생각하고 검사
    for d in dir:
        cnt = 0
        nr = r + dr[d]
        nc = c + dc[d]
        for _ in range(5):  # 현 방향으로 5개 확인
            if not (0 <= nr < 10 and 0 <= nc < 10):
                totalCnt += cnt
                break
            if A[nr][nc] == "X":
                cnt += 1
                nr += dr[d]
                nc += dc[d]
            else:
                totalCnt += cnt
                break
    if totalCnt >= 5:   # 오목 이룸
        return True
    return False

A = [list(input().strip()) for _ in range(10)]
print(solve())