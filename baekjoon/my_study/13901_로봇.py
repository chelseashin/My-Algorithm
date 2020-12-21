import sys
sys.stdin = open('13901_input.txt')
input = sys.stdin.readline

dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)

R, C = map(int, input().split())
k = int(input())
for _ in range(k):
    br, bc = map(int, input().split())
sr, sc = map(int, input().split())
cmd = list(map(int, input().split()))