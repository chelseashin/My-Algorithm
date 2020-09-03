import sys
sys.stdin = open('15684_input.txt')

# 좋은 풀이
# Optimization

def run():
    for sc in range(N):
        r, c = (0, sc)
        while True:
            if r == H:
                break
            if A[r][c] == 1:
                c += 1      # 오른쪽
            elif c > 0 and A[r][c-1] == 1:
                c -= 1      # 왼쪽
            r += 1
        if c != sc:
            return False
    return True

def dfs(depth, sr, K):
    if depth == K:
        # print(A)
        if run():           # 연결 가능 여부
            print(depth)    # 답 찾으면 바로 종료
            exit()
        return
    for r in range(sr, H):
        for c in range(N-1):    # 가장 오른쪽 줄은 추가 X
            # 이미 연결된 경우
            if A[r][c]:
                continue
            if A[r][c-1]:
                continue
            if A[r][c+1]:
                continue
            A[r][c] = 1         # 연결
            dfs(depth+1, r, K)
            A[r][c] = 0         # 해제

# 가로 크기, 최대 가로 대각선 수, 세로 크기
N, M, H = map(int, input().split())

if M == 0:
    print(0)
    exit()

# 연결 가능한 정보를 저장한 리스트
A = [[0] * N for _ in range(H)]
for _ in range(M):
    r, c = map(int, input().split())
    A[r-1][c-1] = 1
# print(A)

for maxDepth in range(4):
    dfs(0, 0, maxDepth)

print(-1)