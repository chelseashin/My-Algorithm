import sys
sys.stdin = open('12100_input.txt')
input = sys.stdin.readline

# 4방향
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(depth):
    global ans
    if depth == 5:
        for i in range(N):
            ans = max(ans, max(board[i]))   # 맵에서 가장 큰 값 리턴
        return
    b = [x[:] for x in B]   # 방향 바꾸기 전 원래의 보드 상태 기억
    for d in range(4):
        move(d)         # 방향으로 이동
        dfs(depth+1)    # 재귀호출
        B = [x[:] for x in b]   # 되돌리기

# main
N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dfs(0)
print(B)
print(ans)