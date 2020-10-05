import sys
sys.stdin = open('19237_input.txt')
input = sys.stdin.readline

# Simulation
# 알고리즘 구현 과정
# 1. 상어들은 현재 위치에 냄새를 뿌림
# 2. 상어 이동 - 이동하는 과정에서 상어 번호 작은 것이 큰 것을 쫓아냄
#   - 우선순위 고려
# 3. 상어가 지나간 곳들의 냄새를 1 감소시킴
#   - 냄새의 값이 0이 되면 해당 위치에 있는 정보 삭제

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def solve():
    time = -1
    while True:
        if time > 1000:
            print(-1)
            return
        # 1번 상어만 남으면 종료
        if len(shark) == 1:
            print(time)
            return
        # 번호가 낮은 것부터 먼저 처리 하기 위해서 정렬
        numbers = sorted(list(shark.keys()))
        # 각 상어의 냄새 뿌리기
        for num in numbers:
            if not A[shark[num][0]][shark[num][1]]:
                # 맵에 상어 번호와 냄새 남은 시간 저장
                A[shark[num][0]][shark[num][1]] = [num, K]
            # 자기 냄새가 있던 칸
            elif A[shark[num][0]][shark[num][1]][0] == num:
                A[shark[num][0]][shark[num][1]] = [num, K]
            else:   # 이동할 수 없으면 삭제
                del shark[num]

        # 상어 이동 - 우선순위 높은 상어 먼저 이동
        numbers = sorted(list(shark.keys()))
        for num in numbers:
            r, c, d = shark[num]    # 상어의 위치, 방향
            flag_blank = False
            for nd in shark_dir[num-1][d-1]:
                nr = r + dr[nd-1]
                nc = c + dc[nd-1]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if not A[nr][nc]:
                    flag_blank = True   # 빈 칸 찾은 상황
                    shark[num] = [nr, nc, nd]   # 상어 이동
                    break
            flag_same = False
            if not flag_blank:      # 빈 칸이 없던 경우라면
                for nd in shark_dir[num-1][d-1]:
                    nr = r + dr[nd-1]
                    nc = c + dc[nd-1]
                    if not (0 <= nr < N and 0 <= nc < N):
                        continue
                    if A[nr][nc][0] == num:     # 똑같은 냄새를 찾은 경우
                        flag_same = True
                        shark[num] = [nr, nc, nd]   # 이동
                        break
            else:
                continue
            if not flag_same:   # 똑같은 냄새도 없으면
                del shark[num]

        # 상어가 지나간 곳 냄새 1 감소
        # 미리 1 감소시키고 새로 이동할 때 K 만큼의 냄새 생성하는 개념
        for i in range(N):
            for j in range(N):
                if A[i][j]:
                    A[i][j][1] -= 1
                    if A[i][j][1] == 0:
                        A[i][j] = 0
        time += 1

# main
# 맵 크기, 상어 수, 냄새 없어지는 시간
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

first_pos = list(map(int, input().split()))
shark = dict()  # 상어의 정보 dict 형태로 저장
for i in range(N):
    for j in range(N):
        if A[i][j]:
            # 상어의 위치(r, c)와 방향정보 저장
            shark[A[i][j]] = [i, j, first_pos[A[i][j]-1]]
            A[i][j] = 0

# 상어 이동방향 우선순위 정보
shark_dir = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]

solve()