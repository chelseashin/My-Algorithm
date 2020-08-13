import sys
sys.stdin = open('17406_input.txt')

# 상태 꼬이지 않도록 copy 잘 사용하기

from itertools import permutations
from copy import deepcopy

# 배열 넣었을 때 행별 최솟값 구하기
def check(arr):
    global MIN
    for i in range(N):
        temp = sum(arr[i])
        if MIN > temp:
            MIN = temp
    return

# def turn():
#     for i in range(size):


N, M, K = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
MIN = float('inf')
print('raw', raw)
calList = [list(map(int, input().split())) for _ in range(K)]
# print('calList', calList)
# 연산 순서 정하기
for L in list(permutations(calList, K)):
    new = [[0] * M for _ in range(N)]
    print(L)
    for cal in L:
        # 연산 후 상태
        temp = deepcopy(new)
        print('ttt', temp)
        r, c, s = cal
        sr, sc = r-s-1, c-s-1
        er, ec = r+s-1, c+s-1
        size = 2 * s + 1
        # r_size, c_size = er-sr+1, ec-sc+1
        print('시작점', sr, sc, '끝점',  er, ec)
        print('돌리는 배열의 크기', size)
        new = [[0] * M for _ in range(N)]
        # turn()
        print('new', new)
        print()
    # check(new)
print(MIN)