import sys
sys.stdin = open('17472_input.txt')

# MST 최소신장트리 공부해보기
# https://gmlwjd9405.github.io/2018/08/28/algorithm-mst.html

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
print(MAP)