import sys
sys.stdin = open('3190_input.txt')

# 다시 풀어보기
# 좋은 풀이
# https://m.post.naver.com/viewer/postView.nhn?volumeNo=26950554&memberNo=33264526

from collections import deque


# main
N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1
# print(board)

M = int(input())
dir_info = [list(input().split()) for _ in range(M)]
# print(dir_info)