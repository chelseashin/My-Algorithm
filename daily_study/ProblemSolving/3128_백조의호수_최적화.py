# 20:00 다른 코드 참고
# 코드 참고 - https://chldkato.tistory.com/58
# 설명 참고 - https://rebas.kr/780
# 와우.... 맵 2개와 큐 4개로 로 다음에 실행할 것을 미리 저장해두고 
# 시행 후 현재 큐와 교환해가며 다음 날을 맞이한다.
# 진짜 많은 것을 배운 문제다.

from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def meltLake():
    while wq:
        r, c = wq.popleft()
        if lake[r][c] == "X":   # 얼음이면
            lake[r][c] = "."    # 녹이기
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if w_check[nr][nc]:     # 이미 물이면
                continue
            w_check[nr][nc] = 1 
            if lake[nr][nc] == "X":         # 다음 위치가 빙판인 경우
                next_wq.append((nr, nc))    # 다음에 물로 녹일 위치 새로운 큐에 담기
            else:
                wq.append((nr, nc))
    # print("w_check 물 체크", wq)
    # for row in w_check:
    #     print(row)

def moveSwan():
    while sq:
        r, c = sq.popleft()
        if (r, c) == (gr, gc):
            # print("친구 만났당!!!!!")
            return True
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 격자 밖이거나 빙판이거나 방문했으면
            if not (0 <= nr < R and 0 <= nc < C) or s_check[nr][nc]:
                continue
            s_check[nr][nc] = 1
            if lake[nr][nc] == ".":     # 물이면 지금 갈 수 있음
                sq.append((nr, nc))
            else:   # 빙판이면 다음에 갈 위치 큐에 담기
                next_sq.append((nr, nc))
    # print("s_check 백조 체크", sq)
    # for row in s_check:
    #     print(row)
    return False

# main
R, C = map(int, input().split())
lake = []
swans = []
s_check = [[0] * C for _ in range(R)]
w_check = [[0] * C for _ in range(R)]
sq, wq, = deque(), deque()
for r in range(R):
    row = list(input().rstrip())
    lake.append(row)
    for c in range(C):
        if row[c] == ".":       # 물
            w_check[r][c] = 1   # 물 체크 배열에 1로 표시
            wq.append((r, c))   # 물 큐(wq)에 담기
        elif row[c] == "L":         # 백조
            swans.append((r, c))    # 백조 위치
            wq.append((r, c))       # 물 큐(wq)에 담기
            lake[r][c] = "."        # 물로 바꾸기

sr, sc = swans[0]   # 백조 1
gr, gc = swans[1]   # 백조 2
sq.append((sr, sc))
s_check[sr][sc] = 1

next_sq, next_wq = deque(), deque()
days = 0
while True:
    
    meltLake()  # 호수 녹이기
    if moveSwan():
        print(days)
        break
    sq, wq = next_sq, next_wq
    next_sq, next_wq = deque(), deque()
    days += 1
    # print("호수 상태 =====================================")
    # for row in lake:
    #     print(row)