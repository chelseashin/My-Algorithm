import sys
sys.stdin = open('5644_input.txt')

from collections import deque

# 상 우 하 좌
dr = (0, -1, 0, 1, 0)
dc = (0, 0, 1, 0, -1)

# BC 설치, 범위와 성능 표시
def install(idx, sr, sc, coverage, performance):
    visited = [[0] * 10 for _ in range(10)]
    visited[sr][sc] = 1
    raw[sr][sc].append((performance, idx))
    Q = deque([(sr, sc)])
    for _ in range(coverage):
        lq = len(Q)
        for __ in range(lq):
            r, c = Q.popleft()
            for dir in range(1, 5):
                nr = r + dr[dir]
                nc = c + dc[dir]
                if not (0 <= nr < 10 and 0 <= nc < 10):
                    continue
                if visited[nr][nc]:
                    continue
                visited[nr][nc] = 1
                raw[nr][nc].append((performance, idx))
                Q.append((nr, nc))

# main
T = int(input())
for tc in range(T):
    M, N = map(int, input().split())    # 이동정보 수, 설치된 BC 수
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    raw = [[[] for _ in range(10)] for _ in range(10)]
    result = 0
    # BC 정보 저장
    for i in range(N):
        x, y, C, P = map(int, input().split())
        install(i, y-1, x-1, C, P)
    
    for i in range(10):
        for j in range(10):
            raw[i][j].sort(reverse=True)    # 내림차순

    # 사용자 A, B 좌표
    ar, ac = 0, 0
    br, bc = 9, 9
    for i in range(M+1):
        # a 없고 b만 있으면 b만 더함
        if not raw[ar][ac]:
            if raw[br][bc]:
                result += raw[br][bc][0][0]
        # b 없고 a만 있으면 a만 더함
        elif not raw[br][bc]:
            if raw[ar][ac]:
                result += raw[ar][ac][0][0]
        # a, b 가장 큰 충전량의 번호가 다르면 가장 큰 거 두개 더함
        elif raw[ar][ac][0][1] != raw[br][bc][0][1]:
            result += raw[ar][ac][0][0] + raw[br][bc][0][0]
        # a, b 가장 큰 충전량의 번호가 같으면 중복이기 때문에
        # 가장 큰 값 + 두 번째로 큰 값들끼리 비교해서 큰 값을 더해줌
        else:
            temp = 0
            if len(raw[ar][ac]) > 1:
                temp = raw[ar][ac][1][0]
            if len(raw[br][bc]) > 1:
                temp = max(temp, raw[br][bc][1][0])
            result += raw[ar][ac][0][0] + temp
        if i == M:
            break
        # 사용자 이동
        dir = A[i]
        ar += dr[dir]
        ac += dc[dir]
        dir = B[i]
        br += dr[dir]
        bc += dc[dir]
        # print(i, (ar, ac), (br, bc), result)

    print("#{} {}".format(tc+1, result))

    # 1 1200
    # 2 3290
    # 3 16620
    # 4 40650
    # 5 52710