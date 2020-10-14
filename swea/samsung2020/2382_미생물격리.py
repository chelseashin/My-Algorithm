import sys
sys.stdin = open('2382_input.txt')

# 상하좌우
dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)
rev = (0, 2, 1, 4, 3)

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(K)]
    for _ in range(M):  # 시간 흐름
        info = dict()  # 미생물의 크기, 방향정보
        for row in range(K):    # 모든 미생물 정보
            r, c, k, d = A[row]
            if not k:
                continue
            # 이동
            nr = r + dr[d]
            nc = c + dc[d]
            A[row][0], A[row][1] = nr, nc
            if not (1 <= nr < N-1 and 1 <= nc < N-1):
                A[row][2] //= 2      # 반감
                A[row][3] = rev[d]   # 방향 전환
            # 아무도 방문하지 않았다면
            if (nr, nc) not in info.keys():
                info[(nr, nc)] = [row, k]

            # 이미 방문했다면
            else:
                num, size = info[(nr, nc)]
                # 현재 군집의 크기가 크다면 기존을 흡수
                if A[row][2] > size:
                    info[(nr, nc)] = [row, k]  # 새로 등록
                    A[row][2] += A[num][2]
                    A[num][2] = 0  # 기존 군집 제거
                # 기존 군집의 크기가 크다면 흡수 당함
                else:
                    A[num][2] += A[row][2]
                    A[row][2] = 0
    # 남아있는 미생물 수 확인
    microbe = 0
    for m in A:
        microbe += m[2]
    print("#{} {}".format(tc+1, microbe))
    
    # 1 145
    # 2 5507
    # 3 9709
    # 4 2669
    # 5 3684
    # 6 774
    # 7 4797
    # 8 8786
    # 9 1374
    # 10 5040
