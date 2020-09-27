n = 19
edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]


def dfs(cnt, n, G, Q, answer):
    nextGoal = []
    nextQ = []
    cnt += len(Q)

    if cnt >= answer[0]:
        return

    if len(Q) == 0:
        answer[0] = min(answer[0], cnt)
        return

    for i in Q:
        for j in range(n):
            if G[i][j]:
                nextGoal.append((i, j))
                nextQ.append(j)

    for i in range(len(nextGoal)):
        s, e = nextGoal[i]

        G[s][e] = 0
        dfs(cnt, n, G, nextQ[:i] + nextQ[i + 1:], answer)
        G[s][e] = 1


def solution(n, edges):
    answer = [987654321]
    G = [[0] * n for _ in range(n)]
    for s, g in edges:
        G[s][g] = 1
    answer = dfs(0, n, G, [0], answer)

    return answer[0]