# 문제 유형 : 힙, 위상정렬
# 전형적인 '위상 정렬' 문제
# 위상정렬(Topology Sort) : 순서가 정해져 있는 작업을 차례로 수행해야 할 때,
# 순서를 결정해주는 알고리즘
# 위상정렬의 시간 복잡도 : O(V+E)로 문제 해결(노드의 갯수 + 간선의 갯수)

import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
A = [[] for _ in range(N+1)]    # 모든 노드에 대해 어떤 노드를 자식 노드로 갖는지 정보를 담음
indegree = [0] * (N+1)          # 진입차수 정보

heap = []
result = []

for _ in range(M):
    x, y = map(int, input().split())
    A[x].append(y)      # 간선 연결
    indegree[y] += 1    # 진입차수 몇인지 계산

for i in range(1, N+1):
    if indegree[i] == 0:    # 진입차수가 0인 정점을 큐에 삽입
        heapq.heappush(heap, i)

while heap:
    num = heapq.heappop(heap)
    result.append(num)
    for j in range(num):    # 꺼낸 데이터에서 이동할 수 있는 정점들 확인
        indegree[j] -= 1    # 진입차수 1씩 감소
        if indegree[j] == 0:    # 뺀 후 진입차수가 0으로 바뀌면 힙에 삽입
            heapq.heappush(heap, j)

print(*result)  # 힙에서 꺼낸 원소 순서대로 출력