import sys
sys.stdin = open('2382_input.txt')

# dfs로 풀이
# https://github.com/gogumasitda/TIL/blob/master/algorithm/0430/%EB%AF%B8%EC%83%9D%EB%AC%BC%EA%B2%A9%EB%A6%AC.py

# main
T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(K)]