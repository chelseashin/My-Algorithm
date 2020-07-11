# 성공 2
# 가장 직관적인 코드

def dfs(depth):
    global board, visited, N, cnt
    if depth == N:
        cnt += 1
        return
    # 열 검사
    for col in range(N):
        if visited[col]:
            continue
        # 대각선 검사
        # 인덱스의 합과 차가 같은 대각선상에 있을 때 같다는 것을 이용함
        # for - else 를 이용해보자
        for r, c  in result:
            if abs(r-depth) == abs(c-col):
                break
        else:
            visited[col] = 1
            result.append((depth, col))
            dfs(depth + 1)
            visited[col] = 0
            result.pop()

N = 8
# N = int(input())
cnt = 0

board = [[0] * N for _ in range(N)]
visited = [0] * N
result = []
dfs(0)
print(cnt)