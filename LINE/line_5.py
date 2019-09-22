import sys
sys.stdin = open('line_5.txt')

# 좌 우 상 하
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def dfs(sr, sc):
    global distance, result
    S = [(sr, sc)]

    while S:
        r, c = S.pop()
        if arr[r][c] == 2:
            result = 1
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (A > nr >= 0 and B > nc >= 0):
                continue
            if arr[nr][nc] == 1:
                continue
            S.append((nr, nc))
            distance += 1
            arr[nr][nc] = 1

A, B = map(int, input().strip().split(' '))
R, C = map(int, input().strip().split(' '))

arr = [[0] * (B+1) for _ in range(A+1)]
arr[R][C] = 2
# print(arr)
distance = 0
result = 0

dfs(0, 0)
print(distance)
print(result)