# 이분그래프는 간단하게 말하면,
# 각 정점을 칠할 수 있는 빨간색과 파란색이 존재할 때
# 인접한 두 정점을 반드시 다른 색으로 칠할 수 있는지를 물어보는 문제

import sys
sys.stdin = open('1707_input.txt')

from collections import deque

# 근데 좀 어렵다.. 다시 공부해보자 이건!
def bfs(start):
    global flag, visited, color
    color[start] = 1
    Q = deque([start])
    while Q and flag:
        s = Q.popleft()
        c = color[s]
        if visited[s]:
            continue
        visited[s] = 1
        for link in G[s]:
            if visited[link] and color[s] == color[link]:
                flag = False
                break
            elif not visited[link]:
                color[link] = -c
                Q.append(link)

# main
K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    color = [0] * (V+1)
    visited = [0] * (V+1)
    flag = True
    
    # 연결 정보 리스트
    G = [[] for _ in range(V + 1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        G[v1].append(v2)
        G[v2].append(v1)

    for i in range(1, V+1):
        if not flag:
            break
        if not visited[i]:
            bfs(i)

    if flag:
        print('YES')
    else:
        print('NO')