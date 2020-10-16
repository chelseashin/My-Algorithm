import sys
sys.stdin = open('5653_input.txt')

# 1. X 시간동안 비활성
# 2. X 시간 지나는 순간 활성 => 활성되는 순간 4방향 번식
# (이미 있으면 번식X, 동시에 도달하면 생명력 높은 세포로)
# 3. X 시간 후에 죽음
# K 시간 후 살아있는 줄기 세포(비활성상태 + 활성상태)의 총 개수를 구해라.

from heapq import heappush, heappop

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# main
T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    aliveLst = []   # pq
    visit = {}
    for i in range(N):
        A = list(map(int, input().split()))
        for j in range(M):
            if A[j]:
                # 현재 남은 시간, 활성화여부(0, 1), 좌표, 생명력
                heappush(aliveLst, [A[j], 0, i, j, A[j]])
                visit[i, j] = 1
    # print('visit', visit)
    # print('aliveLst', len(aliveLst), aliveLst)
    for t in range(1, K+1):     # K 시간동안
        activeLst = {}
        while aliveLst:
            # 남은 생명 낮은 순으로 pop
            cur, f, r, c, life = heappop(aliveLst)
            if cur > t:
                heappush(aliveLst, [cur, f, r, c, life])
                break
            else:
                if not f:   # 비활성이면 활성으로
                    heappush(aliveLst, [life+t, 1, r, c, life])
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if (nr, nc) in visit:
                            continue
                        # 이미 있다면 생명력 높은 세포로
                        if (nr, nc) in activeLst:
                            activeLst[nr, nc] = max(activeLst[nr, nc], life)
                        else:
                            activeLst[nr, nc] = life

        # print(t, '초 후 =============================')
        # print('visit', visit)
        # print('aliveLst', len(aliveLst), aliveLst)
        # print('activeLst', len(activeLst), activeLst)
        if t == K:  # K 시간 까지이기 때문
            continue
        for [r, c], life in activeLst.items():
            visit[r, c] = 1
            heappush(aliveLst, [t+life+1, 0, r, c, life])
    print("#{} {}".format(tc+1, len(aliveLst)))