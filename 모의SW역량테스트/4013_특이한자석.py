import sys
sys.stdin = open("4013_input.txt")

def dfs(pos, dir):
    global mag, turn
    visited[pos] = 1
    # 양쪽에 있는 것들은 반대방향
    if (pos > 0):
        if mag[pos][6] != mag[pos-1][2] and visited[pos-1] == 0:
            dfs(pos-1, -dir)
    if (pos < 3):
        if mag[pos][2] != mag[pos+1][6] and visited[pos+1] == 0:
            dfs(pos+1, -dir)

    # 시계방향
    if dir == 1:
        mag[pos] = [mag[pos][-1]] + mag[pos][:-1]

    # 반시계방향
    else:
        mag[pos] = mag[pos][1:] + [mag[pos][0]]


T = int(input())
for tc in range(T):
    K = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]
    turn = [list(map(int, input().split())) for _ in range(K)]
    # print(K, turn)
    for i in range(K):
        visited = [0] * 4
        n = turn[i][0]    # 위치
        d = turn[i][1]    # 방향
        dfs(n-1, d)

    score = 1*mag[0][0] + 2*mag[1][0] + 4*mag[2][0] + 8*mag[3][0]
    print("#{} {}".format(tc+1, score))