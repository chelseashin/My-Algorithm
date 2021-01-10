mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import heapq

# 그래프 정보와 시작점을 받음
def dijkstra(graph, start):
    # 시작 정점에서 각 정점까지의 거리를 저장할 딕셔너리 생성, 무한대('inf')로 초기화
    distances = {node: float('inf') for node in graph}
    
    # 그래프의 시작 정점의 거리 0으로 초기화
    distances[start] = 0
    
    # 모든 정점이 저장될 우선순위 큐 생성
    queue = []
    
    # 그래프의 시작 정점과 시작 정점의 거리(0)을 최소힙에 넣어줌
    heapq.heappush(queue, [distances[start], start])    # 첫 값 넣기

    while queue:

        # 큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트
        current_distance, current_node = heapq.heappop(queue)

        # 현재 최단거리에 있는 거리보다 크다면 무시. 더 볼 필요 X
        if distances[current_node] < current_distance:
            continue

        # 인접한 노드 이름, 노드에 접근하는 거리값
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            # 만약 시작 정점에서 인접 정점으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 가까울 경우에는
            if distance < distances[adjacent]:
                # 최단 거리 업데이트
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances

print(dijkstra(mygraph, 'A'))