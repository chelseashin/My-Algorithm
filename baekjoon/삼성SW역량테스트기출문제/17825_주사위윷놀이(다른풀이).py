import sys
sys.stdin = open('17825_input.txt')

# 참고 링크
# https://calmlife.tistory.com/17

A = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
     [10, 13, 16, 19],
     [20, 22, 24],
     [30, 28, 27, 26],
     [25, 30, 35, 40]]

def solve(depth, score):
    global horse, visited, done, res
    if depth == 10:
        res = max(res, score)
        return
    h = [x[:] for x in horse]
    v = [x[:] for x in visited]
    for i in range(4):
        d, x = horse[i]  # 시작하는 말의 방향과 인덱스
        prev = move[depth]
        nd = d
        nx = x + prev
        if x == done:    # 이미 도착한 말이면
            continue
        # d가 0이고(테두리), 확인할 index가 내부에 들어갈 인덱스면
        if d == 0 and (x in [5, 10, 15]):
            nd = x // 5
            nx = prev
        if nd == 0 and nx == 20:
            nd = 4
            nx = 3
        if nd in [1, 2, 3] and (len(A[nd]) <= nx):
            nx = nx - len(A[nd])
            nd = 4
        if len(A[nd]) <= nx:
            horse[i] = [0, done]
            visited[d][x] = 0
            solve(depth+1, score)   # 도착했으면 더해줄 것 X
        else:
            if visited[nd][nx]:
                continue
            horse[i] = [nd, nx]     # 말 이동
            visited[nd][nx] = 1
            visited[d][x] = 0
            solve(depth+1, score + A[nd][nx])   # 판 위에 있으면 더해줌
        horse = [x[:] for x in h]
        visited = [x[:] for x in v]
    return res

# main
move = list(map(int, sys.stdin.readline().split()))

res = 0
done = float('inf')
visited = [[0] * 21 for _ in range(5)]  # 1차 : 방향, 2차 : 인덱스
horse = [[0, 0] for _ in range(4)]      # 1차 : 말 번호, 2차 : [방향, 인덱스]

print(solve(0, 0))