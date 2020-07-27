import sys
sys.stdin = open('09_input.txt')

def bfs(sn):
    global K
    Q = [sn]
    visited[sn] = 1
    while Q:
        n = Q.pop(0)
        if n == K:
            print(visited[n]-1)
            return
        for i in range(3):
            if i == 0:
                new_n = n - 1
                if not (0 <= new_n < 100001):
                    continue
                if visited[new_n]:
                    continue
                visited[new_n] = visited[n] + 1
                Q.append(new_n)
            elif i == 1:
                new_n = n + 1
                if not (0 <= new_n < 100001):
                    continue
                if visited[new_n]:
                    continue
                visited[new_n] = visited[n] + 1
                Q.append(new_n)
            else:
                new_n = 2 * n
                if not (0 <= new_n < 100001):
                    continue
                if visited[new_n]:
                    continue
                visited[new_n] = visited[n] + 1
                Q.append(new_n)

N, K = map(int, input().split())
visited = [0] * 100001
bfs(N)
