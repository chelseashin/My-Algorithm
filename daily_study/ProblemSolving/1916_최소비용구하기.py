# 7%에서 시간초과
# dijkstra 알고리즘 사용해야 함...

from sys import stdin
input = stdin.readline

def dfs(start, total):
    global minCost
    if start == end:
        # print(total, check)
        minCost = min(minCost, total)
        return
    for next in busInfo[start]:
        if check[next]:    # 방문 표시 되어 있으면
            continue
        check[next] = check[start] + 1
        dfs(next, total + costTable[start][next])
        check[next] = 0

# main
N = int(input())
M = int(input())
costTable = [[0] * (N+1) for _ in range(N+1)]
busInfo = dict()
for _ in range(M):
    s, e, cost = map(int, input().split())
    if costTable[s][e]:
        costTable[s][e] = min(costTable[s][e], cost)
    else: costTable[s][e] = cost
    if s not in busInfo.keys():
        busInfo[s] = [e]
    else:
        busInfo[s].append(e)

start, end = map(int, input().split())
check = [0] * (N+1)
check[start] = 1
minCost = float('inf')
dfs(start, 0)
print(minCost)

# 반례 - 답 10
# 2
# 2
# 1 2 10
# 1 2 20
# 1 2