# 참고 https://jjangsungwon.tistory.com/28

# 각 노드마다 인접한 간선들을 모두 검사하는 과정은 O(E) 시간이 걸림
# O(E) 개의 노드/거리 정보에 대해
# 우선순위 큐를 유지하는 작업은 O(logE) 가 걸림
# 따라서 다익스트라 시간 복잡도 : O(ElogE)


from sys import stdin, maxsize
input = stdin.readline
from heapq import heappush, heappop

def dijkstra(start, end):
    heapq = []
    heappush(heapq, (0, start))     # (0, 시작 정점) 힙에 추가
    distance = [maxsize] * (N+1)    # 각 정점사이의 거리 무한대로 초기화
    distance[start] = 0             # 시작 지점 0으로 초기화
    while heapq:
        weight, index = heappop(heapq)      # 비용이 가장 작은 간선 pop
        for e, c in busInfo[index]:
            # 배열에 저장되어 있는 거리보다
            # 첫 정점에서 해당 노드로 가는 거리가 더 짧을 경우,
            # 배열에 해당 노드의 거리를 업데이트하고 우선순위 큐에 push 한다.
            if distance[e] > weight + c:
                distance[e] = weight + c
                heappush(heapq, (weight+c, e))
    # print(distance)
    return distance[end]

# main
N = int(input())
M = int(input())
busInfo = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, cost = map(int, input().split())
    busInfo[s].append((e, cost))
# print(busInfo)
start, end = map(int, input().split())

print(dijkstra(start, end))

# 반례 - 답 10
# 2
# 2
# 1 2 10
# 1 2 20
# 1 2