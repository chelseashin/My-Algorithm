import sys
sys.stdin = open('13901_input.txt')
input = sys.stdin.readline

# 상하좌우
dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)

# 방법 1
# 참고 링크 : https://sangdo913.tistory.com/121?category=823156
R, C = map(int, input().split())
room = [[True] * C for _ in range(R)]

k = int(input())    # 장애물 갯수
for _ in range(k):
    br, bc = map(int, input().split())
    room[br][bc] = False
sr, sc = map(int, input().split())
room[sr][sc] = False
cmd = list(map(int, input().split()))

flag = True
cnt = 0
while flag:
    flag = False
    for i in range(4):
        nr = sr + dr[cmd[(cnt + i) % 4]]
        nc = sc + dc[cmd[(cnt + i) % 4]]
        if not (0 <= nr < R and 0 <= nc < C):
            continue
        # 갈 수 있으면
        if room[nr][nc]:
            cnt = (cnt + i) % 4
            room[sr][sc] = False
            sr, sc = nr, nc
            flag = True
            break
    print(flag, cnt)
    for r in room:
        print(r)
print(sr, sc)

# 방법 2
# R, C = map(int, input().split())
# room = [["*"] * C for _ in range(R)]
# k = int(input())    # 장애물 갯수
# for _ in range(k):
#     br, bc = map(int, input().split())
#     room[br][bc] = "X"
# sr, sc = map(int, input().split())
# room[sr][sc] = "0"
# cmd = list(map(int, input().split()))
# i = 0
# cnt = 0
# while True:
#     if cnt == 4:
#         print(sr, sc)
#         break
#     nr = sr + dr[cmd[i]]
#     nc = sc + dc[cmd[i]]
#     if not (0 <= nr < R and 0 <= nc < C) or room[nr][nc] != "*":
#         i = (i+1) % 4
#         cnt += 1
#         continue
#     room[nr][nc] = str(int(room[sr][sc]) + 1)
#     sr, sc = nr, nc
#     cnt = 0
#     print(cmd[i], (nr, nc))
#     for r in room:
#         print(r)