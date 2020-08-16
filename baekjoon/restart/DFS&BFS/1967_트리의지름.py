import sys
sys.stdin = open('1967_input.txt')

# 어렵다... 다시 생각해보자...

# root로부터의 모든 경로 중에서 최대값을 구한다
# 최대값에 해당하는 경로의 끝 지점 인덱스를 구한다.
# 해당 인덱스로부터 이동 경로의 최대값을 구하면 트리의 최대 지름을 구할 수 있다.

from collections import deque

def bfs(s, mode):
    Q = deque()
    Q.append(s)
    visited = [-1 for _ in range(N)]
    visited[s] = 0
    while Q:
        now = Q.popleft()
        for w, next in linked[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + w
                Q.append(next)
    # print(visited)
    if mode == 1:
        return visited.index(max(visited))
    else:
        return max(visited)

# main
N = int(input())
linked = [[] for _ in range(N)]

for _ in range(N-1):
    s, g, w = map(int, input().split())
    linked[s-1].append([w, g-1])
    linked[g-1].append([w, s-1])
# print(linked)

print(bfs(bfs(0, 1), 2))