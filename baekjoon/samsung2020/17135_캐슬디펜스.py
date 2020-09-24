import sys
sys.stdin = open('17135_input.txt')
input = sys.stdin.readline

# Brute Force, Simulation
# 단순하게 생각할 것.

def kill_enemy(select):
    A = [x[:] for x in raw]
    cnt = 0
    for _ in range(N):
        v = set()   # 공격할 적들
        for k in range(3):
            Q = []   # 공격할 적 후보들
            for r in range(N):
                for c in range(M):
                    if A[r][c]:
                        dist = abs(N-r) + abs(select[k]-c)
                        # D 거리 이내에 있으면 Q에 담기
                        if dist <= D:
                            Q.append((r, c, dist))
            if Q:        # 공격할 수 있는 적들 있으면
                # 거리, 왼쪽 순으로 정렬
                Q.sort(key=lambda x: (x[2], x[1]))
                r, c, d = Q.pop(0)
                v.add((r, c))
        for r, c in v:    # v에 담긴 적들 공격
            A[r][c] = 0
            cnt += 1
        # 적들 한 칸씩 내리기
        A.pop()
        A.insert(0, [0] * M)
    return cnt

def comb(depth, k):
    global result
    if depth == 3:
        # print(selected)
        result = max(result, kill_enemy(selected))
        return
    for i in range(k, M):
        selected.append(i)
        comb(depth+1, i+1)
        selected.pop()

# main
N, M, D = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
result = float('-inf')

selected = []
comb(0, 0)
print(result)