# 플로이드 와샬! 이라는 알고리즘이 있다고 한다.
# 처음 혼자 힘으로 금방 풀었지만, 스스로 엣지 케이스를 여러개 생각해냈고
# 이를 만족시키기 위한 알고리즘이 필요하다고 느꼈다. ==> 플로이드 와샬

import sys
input = sys.stdin.readline

# x번에서 y번으로 갈 때의 거리
def distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def near(num):
    where = -1   # 거리가 가까운 번호
    temp = -1
    for i in range(N):
        if not s[i]:    # 특별한 도시가 아니라면
            continue
        if temp == -1 or info[num][i] < temp:
            temp = info[num][i]
            where = i
    return where


def shortest_path(start, goal):
    dis = info[start][goal]    # 기본 거리

    if s[start] == 1 and s[goal] == 1:   # 둘 다 특별한 도시라면
        dis = min(T, dis)

    near_s = near(goal)
    near_g = near(start)
    if near_s != -1 and near_g != -1:
        temp = info[start][near_g] + T + info[near_s][goal]
        if dis > temp:
            dis = temp
    return dis

# main
N, T = map(int, input().split())
s = [0] * N
a = []
for n in range(N):
    s[n], r, c = map(int, input().split())
    a.append((r, c))
# print(s)
# print(a)

info = [[0] * N for _ in range(N)]      # i 번에서 j 번으로 갈 때 최단거리
for i in range(N-1):
    for j in range(i+1, N):
        if i == j:
            continue
        info[i][j] = info[j][i] = distance(a[i], a[j])
# for i in info:
#     print(i)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(shortest_path(a-1, b-1))