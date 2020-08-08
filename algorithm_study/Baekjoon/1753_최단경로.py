import sys
sys.stdin = open('1753_input.txt')

# 다익스트라 알고리즘
# 한 꼭짓점을 "소스" 꼭짓점으로 고정하고
# 그래프의 다른 모든 꼭짓점까지의 최단경로를 찾는 알고리즘
# 최단 경로 트리를 만드는 것

from heapq import heappush, heappop

# 다익스트라 기본 알고리즘 - 각 정점별로 최단경로 구하기
def dijkstra(v, k, graph):
    dist = [INF] * v
    dist[k-1] = 0
    Q = []
    heappush(Q, [0, k-1])
    while Q:
        # print(Q)
        cost, pos = heappop(Q)
        for p, c in graph[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heappush(Q, [c, p])
    return dist

V, E = map(int, input().split())
K = int(input())
G = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u-1].append([v-1, w])
# print(G)

# 정점 갯수, 시작점, 그래프
INF = float('inf')
for d in dijkstra(V, K, G):
    if d != INF:
        print(d)
    else:
        print("INF")