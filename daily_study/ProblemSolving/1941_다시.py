from sys import stdin
input = stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def check():
    temp = 1
    visited = [[0] * 5 for _ in range(5)]
    sr, sc = order[0]//5, order[0]%5
    visited[sr][sc] = 1
    stack = [(sr, sc)]
    
    while stack:
        r, c = stack.pop()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < 5 and 0 <= nc < 5) or visited[nr][nc]:
                continue
            nextNum = nr*5 + nc
            if nextNum in set(order):
                visited[nr][nc] = 1
                stack.append((nr, nc))
                temp += 1
    return temp

def comb(depth, ycnt, k):
    global total, result
    if ycnt > 3 or 25-k < 7-depth:
        return

    if depth == 7:
        total += 1
        if check() == 7:
            result += 1
            # print(order)
        return

    for idx in range(k, 25):
        r = idx // 5
        c = idx % 5
        if A[r][c] == "Y":
            order[depth] = idx
            comb(depth+1, ycnt+1, idx+1)
            order[depth] = 0
        else:
            order[depth] = idx
            comb(depth+1, ycnt, idx+1)
            order[depth] = 0


# main
A = [input().rstrip() for _ in range(5)]

result = 0
order = [0] * 7
total = 0
comb(0, 0, 0)
print(result)
# print(total)