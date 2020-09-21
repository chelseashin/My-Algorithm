import sys
sys.stdin = open('12100_input.txt')
input = sys.stdin.readline
from collections import deque

# 비교하려는 idx값이 없으면 => 이전에 추가된 값이 없으므로 값만 추가해준다. 
# idx는 그대로 둔다.
# 비교하려는 idx값이 있으면 => 이전에 추가된 값과 비교하고 idx를 1 올려준다. 
# 만약 비교값이 같으면 합쳐지는 것이므로 두 배 해주고, 다르면 새로운 값을 추가해준다.
def cal(r, c, dr, dc):
    global B, ans
    Q = deque()
    idx = 0
    nr, nc = r, c   # 첫 위치 기억
    while True:
        if not (0 <= nr < N and 0 <= nc < N):
            break
        if B[nr][nc]:
            if idx >= len(Q):
                Q.append(B[nr][nc])
            else:
                if Q[idx] == B[nr][nc]:
                    Q[idx] *= 2
                    ans = max(ans, Q[idx])      # 최댓값 갱신
                else:
                    Q.append(B[nr][nc])
                idx += 1
        nr += dr
        nc += dc
    for i in range(N):
        if Q:
            B[r][c] = Q.popleft()
        else:
            B[r][c] = 0
        r += dr
        c += dc

# 탐색 방향 주의!!!!
def move(d):
    for i in range(N):
        if d == 0:      # 좌
            cal(i, 0, 0, 1)
        elif d == 1:    # 상
            cal(0, i, 1, 0)
        elif d == 2:    # 우
            cal(i, N-1, 0, -1)
        elif d == 3:    # 하
            cal(N-1, i, -1, 0)

# 완전탐색
def solve(cnt):
    global B
    if cnt == 5:    # 최대 5번 이동
        return
    A = [x[:] for x in B]
    for i in range(4):
        move(i)
        solve(cnt+1)
        B = [x[:] for x in A]

# main
N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    ans = max(ans, max(B[i]))
solve(0)
print(ans)