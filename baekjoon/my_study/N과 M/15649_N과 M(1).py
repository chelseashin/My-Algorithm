# N, M = map(int, input().split())
N, M = 4, 4

# 순열 구현 기본 코드
def perm(depth, k):
    if depth == M:
        print(*order)
        return
    for i in range(k, N+1):
        if visited[i]:
            continue
        visited[i] = 1
        order.append(i)
        perm(depth+1, k)
        order.pop()
        visited[i] = 0

order = []
visited = [0] * (N+1)
# perm(0, 1)

# 순열 라이브러리 사용 기본 코드
from itertools import permutations
for x in list(permutations(range(1, N+1), M)):
    print(*x)