import sys
sys.stdin = open('2105_input.txt')

# 다른 풀이

# 각 변의 길이를 num 리스트에 넣어서
# 마주보는 변의 길이가 같을 때
# 가능한 경우인지 check 함수로 확인

# 우하, 좌하, 좌상, 우상
dr = (1, 1, -1, -1)
dc = (1, -1, -1, 1)

def check(r, c):
    global MAX, M
    temp = []
    cnt = 0
    for i in range(4):
        for j in range(num[i]):
            r = r + dr[i]
            c = c + dc[i]
            if M[r][c] not in temp:
                temp.append(M[r][c])
                cnt += 1
            else:
                return
    MAX = max(MAX, cnt)

def dfs(dir, r, c):
    if dir > 2:
        if num[0] != num[2]:
            return

    if dir == 4:
        if num[0] == num[2] and num[1] == num[3]:
            check(sr, sc)
        return

    for dis in range(N-1, 0, -1):
        nr = r + dr[dir] * dis
        nc = c + dc[dir] * dis
        if (0 <= nr < N and 0 <= nc < N):
            num[dir] = dis
            dfs(dir+1, nr, nc)

# main
T = int(input())
for tc in range(T):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    num = [0, 0, 0, 0]
    MAX = -1

    for i in range(N-2):
        for j in range(1, N-1):
            sr, sc = i, j
            dfs(0, sr, sc)

    print("#{} {}".format(tc + 1, MAX))