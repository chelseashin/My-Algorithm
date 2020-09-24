import sys
sys.stdin = open('17135_input.txt')
input = sys.stdin.readline

# 참고 링크 : https://rebas.kr/835
# 단순하게 생각할 것.
# 우선순위 큐 heapq 이용

from heapq import heappush, heappop

def kill_enemy():
    global archer
    A = [x[:] for x in raw]
    cnt = 0
    for _ in range(N):
        v = set()           # 한 턴에 죽일 수 있는 적들
        for k in range(3):  # 궁수 3명
            Q = []          # 죽일 수 있는 적의 후보들
            for r in range(N):
                for c in range(M):
                    if A[r][c]:     # 적 있을 경우 거리 계산
                        dist = abs(N-r) + abs(archer[k]-c)
                        # 거리가 D 이하이면 우선순위 큐에 넣는다
                        # 우선순위 큐 dis, c, r 순으로 자동정렬
                        if dist <= D:
                            heappush(Q, (dist, c, r))
            if Q:
                d, c, r = heappop(Q)
                v.add((r, c))
        for r, c in v:
            A[r][c] = 0     # 적 죽이기
            cnt += 1
        # 적 한 칸씩 내리기
        for i in range(N-2, -1, -1):
            for j in range(M):
                A[i+1][j] = A[i][j]
        A[0] = [0] * M
    return cnt

# main
N, M, D = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
result = float('-inf')

archer = [0] * 3
for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            archer = [i, j, k]
            result = max(result, kill_enemy())

print(result)