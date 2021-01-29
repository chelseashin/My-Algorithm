# 문제 정리 : 시작섬에서 도착섬까지 운반할 수 있는 '최대 중량'을 구하는 것
# 사용 알고리즘 : BFS + 이진탐색
# 다리의 갯수 M은 최대 100,000이며, 중량제한 C는 최대 1,000,000,000(10억)이다.
# 이진 탐색을 이용하여 O(M*logC)에 문제 해결 가능
# 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 이진탐색으로 찾는다.
# 찾고자 하는 중량 제한의 최댓값을 이진탐색으로 찾자.

from collections import deque

def bfs(temp):
    Q = deque([start_node])
    visited = [0] * (N+1)
    visited[start_node] = 1
    while Q:
        x = Q.popleft()
        for y, weight in adj[x]:
            # 갈 수 있는 곳이면서 무게 제한이 걸리지 않을 경우
            if not visited[y] and weight >= temp:
                visited[y] = True
                if visited[end_node]:
                    return 1
                Q.append(y)
    return 0    # 끝점에 도착하면 1 아니면 0을 리턴

# main
N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]

# 통과할 수 있는 무게의 시작값과 끝값을 지정.
start = 1000000000
end = 1

# 각 도시의 연결 여부와 무게 제한을 저장하는 adj 배열 생성
for _ in range(M):
    x, y, weight = map(int, input().split())
    adj[x].append((y, weight))
    adj[y].append((x, weight))
    start = min(start, weight)
    end = max(end, weight)

# 시작섬, 도착섬
start_node, end_node = map(int, input().split())

# 이분탐색으로 최댓값 찾기
result = start
while start <= end:
    mid = (start + end) // 2
    # 해당 무게로 start_node에서 end_node까지 도착이 가능한 경우
    if bfs(mid):
        result = mid          # result를 mid로 갱신
        start = mid + 1       # 시작값을 mid + 1로 바꿈
    else:
        end = mid - 1         # 불가능하다면 끝 값을 1씩 줄이며 확인 
print(result)