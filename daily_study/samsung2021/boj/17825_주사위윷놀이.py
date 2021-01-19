# from 11:17 to
# h m
# 참고 링크 : https://calmlife.tistory.com/17

# 말 4개로 게임
# 이동한 후의 위치에 이미 말이 있으면 갈 수 없다.
# 말이 이동해 있을 수 있는 각 칸의 점수의 합의 최댓값
# 10, 20, 30번 위치에서는 무조건 안쪽 화살표로 들어가도록

import sys
input = sys.stdin.readline


board = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38],
         [13, 16, 19],
         [22, 24],
         [28, 27, 26],
         [25, 30, 35],
         [40]
         ]

def dfs(depth, score):
    global MAX
    if depth == 10:
        MAX = max(MAX, score)
        return


move = list(map(int, input().split()))
print(move)
MAX = float('-inf')
horse = [[0, 0, 0] for _ in range(4)]

dfs(0, 0)