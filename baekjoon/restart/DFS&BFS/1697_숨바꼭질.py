# N의 범위 조심
# 인덱스 잘 따져보기
# 조건 확인
# 일차원상의 간단한 bfs 문제

def bfs(s):
    global N, K, visited
    Q = [s]
    visited[s] = 1
    while Q:
        ns = Q.pop(0)
        if ns == K:
            print(visited[ns]-1)
            # print(visited)
            return
        for i in range(3):
            if i == 0:
                new_n = ns + 1
                if not (0 <= new_n < 100001):
                    continue
                if visited[new_n] == 0:
                    visited[new_n] = visited[ns] + 1
                    Q.append(new_n)
            elif i == 1:
                new_n = ns - 1
                if not (0 <= new_n < 100001):
                    continue
                if visited[new_n] == 0:
                    visited[new_n] = visited[ns] + 1
                    Q.append(new_n)
            else:
                new_n = ns * 2
                if not (0 <= new_n < 100001):
                    continue
                if visited[new_n] == 0:
                    visited[new_n] = visited[ns] + 1
                    Q.append(new_n)

N, K = 5, 17
# N, K = map(int, input().split())
visited = [0] * 100001
bfs(N)