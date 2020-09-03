import sys
sys.stdin = open('15684_input.txt')

# 1. 연결을 저장하는 리스트 a를 만든다
#    a는 2차 리스트인데 a[세로][가로] 로 사용한다
#    따라서 a의 크기는 n x h이다
# 2. a에 연결 관계를 저장한다
#    a[r-1][c-1]은 r-1번째 세로일 때 c-1번째 가로에서 r번째 가로로 이동할 수 있음을 의미한다
# 3. dfs로 구현한 조합으로 어느 가로선을 연결할 지 정한다
# 4. dfs에서 연결할 선을 고를 때 다른 가로선과 이어지면 안되는 조건을 고려해야 한다
#    현재 위치를 세로i , 가로j 라고 할 때 i-1번 째 세로와 i+1번 째 세로에 연결된 가로선이 있는지 확인한다
# 5. 연결할 가로선을 모두 고르면 check 함수를 실행해서 출발한 세로선과 도착한 세로선의 인덱스가 같은지 확인한다
# 6. 만일 같으면 ans에 가로선을 고른 개수를 바로 return
# 7. 그렇지 않으면 -1 return

def check():
    for sc in range(N):
        c = sc
        for r in range(H):
            if A[r][c]:
                c += 1      # 오른쪽으로 이동
            elif A[r][c-1]:
                c -= 1      # 왼쪽으로 이동
        if sc != c:
            return False
    return True

def dfs(depth, row, K):
    global ans
    if depth == K:
        # print(A)
        if check():       # 답 찾으면 바로 종료
            print(depth)
            exit()
        return
    for i in range(row, H):
        for j in range(N-1):
            if A[i][j]:
                continue
            if A[i][j-1]:
                continue
            if A[i][j+1]:
                continue
            A[i][j] = 1
            dfs(depth+1, i, K)
            A[i][j] = 0

# main
# 가로 크기, 최대 가로 대각선 수, 세로 크기
N, M, H = map(int, input().split())

if M == 0:
    print(0)
    exit()

A = [[0] * N for _ in range(H)]
for i in range(M):
    r, c = map(int, input().split())
    A[r-1][c-1] = 1

ans = -1
for maxDepth in range(4):
    dfs(0, 0, maxDepth)

print(ans)