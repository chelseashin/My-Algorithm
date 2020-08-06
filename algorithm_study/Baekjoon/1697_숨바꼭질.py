N, K = 5, 17
from collections import deque

# N, K = map(int, input().split())

dist = [-1] * 100002
dist[N] = 0
Q = deque()
Q.append(N)
while dist[K] == -1:
    temp = Q.popleft()
    for next in (temp-1, temp+1, 2*temp):
        if not (0 <= next < 100001):
            continue
        if dist[next] != -1:
            continue
        dist[next] = dist[temp] + 1
        Q.append(next)
# print(dist)
print(dist[K])