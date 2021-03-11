# 19:10 start
# 19:51 finish

import sys
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

R, C = map(int, input().split())
A = [list(input().strip()) for _ in range(R)]

flag = 0
for r in range(R):
    for c in range(C):
        # 늑대일 때
        if A[r][c] == "W":
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < R and 0 <= nc < C):
                    continue
                elif A[nr][nc] == "S":      # 늑대와 양이 인접하면 불가능
                    flag = 1
                    break
        elif A[r][c] == ".":    # 빈 공간은 모두 울타리 설치
            A[r][c] = "D"

    # 한 행 탐색 끝났을 때 flag가 1이라면 이미 불가능하므로 0 출력
    if flag:
        print(0)
        break

if not flag:
    print(1)
    for row in A:
        print(''.join(row))