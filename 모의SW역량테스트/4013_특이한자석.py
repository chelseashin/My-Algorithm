import sys
sys.stdin = open("4013_input.txt")

def dfs(pos, dir):
    global mag, turn
    visited[pos] = 1
    # 양쪽에 있는 것들은 반대방향

    # 같은 쪽에 있는 것들은 같은 방향



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
    # print("#{} {}".format(tc+1, score))