from sys import stdin
input = stdin.readline

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

def dfs(depth, r, c, percentage):
    global result
    if depth == N:
        # print(check, percentage)
        result += percentage
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if (nr, nc) in check:
            continue
        check.append((nr, nc))
        dfs(depth+1, nr, nc, percentage*dirInfo[i])
        check.pop()

# main
N, east, west, south, north = map(int, input().split())
dirInfo = [east/100, west/100, south/100, north/100]

result = 0
check = [(0, 0)]
dfs(0, 0, 0, 1)
print(result)