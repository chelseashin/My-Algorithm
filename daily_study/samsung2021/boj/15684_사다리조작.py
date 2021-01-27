# 09:15 start
# 10:25 end
# 1h 10m
# 조금만 생각하면 쉬운 문제. 단, 인덱스 꾸준히 신경써야 함
# 가로선 놓을 수 있는 모든 경우의 수 고려 => 완전탐색

def ladder():
    for sc in range(N):
        r, c = 0, sc        # 시작 열 sc
        while True:
            if r == H:      # 마지막 행 도착하면 종료
                break
            if A[r][c]:     # 오른쪽 열로 이동
                c += 1
            elif c > 0 and A[r][c-1]:   # 왼쪽 열로 이동
                c -= 1
            r += 1
        if sc != c:         # 마지막 행에 도착 후 다른 번호라면
            return False
    return True             # 모든 열이 자기 번호 도착 성공

def dfs(depth, sr, K):
    if depth == K:
        if ladder():        # 각자 자기 번호로 도착 성공
            print(depth)    # 바로 depth 출력 후 종료
            exit()
        return

    for r in range(sr, H):
        for c in range(N-1):
            if A[r][c] or A[r][c-1] or A[r][c+1]:   # 두 가로선 연속 X
                continue
            A[r][c] = 9     # 가로선 추가
            dfs(depth+1, r, K)
            A[r][c] = 0

# main
N, M, H = map(int, input().split())
if M == 0:
    print(0)
    exit()

A = [[0] * N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    A[a-1][b-1] = 1


for maxDepth in range(4):
    dfs(0, 0, maxDepth)
print(-1)