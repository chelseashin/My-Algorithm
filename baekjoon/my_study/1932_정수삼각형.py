import sys
sys.stdin = open("1932_input.txt")
input = sys.stdin.readline

def dfs(depth, idx, temp):
    global MAX, N
    if depth == N:
        MAX = max(MAX, temp)
        print(temp)
        return
    for i in range(idx, idx+2):
        dfs(depth+1, i, temp + T[depth][i])

# main
N = int(input())
T = [list(map(int, input().split())) for _ in range(N)]
MAX = 0
# 실패
# dfs(1, 0, T[0][0])
# print(MAX)

for i in range(1, N):
    for j in range(len(T[i])):
        # 삼각형 왼쪽 변
        if j == 0:
            T[i][j] += T[i-1][j]
        # 삼각형 오른쪽 변
        elif j == i:
            T[i][j] += T[i-1][j-1]
        else:
            # 삼각형 안쪽 부분, 겹치는 부분은 윗줄의 두 수 중 큰 수에 더해줌
            T[i][j] += max(T[i-1][j], T[i-1][j-1])

print(max(T[-1]))