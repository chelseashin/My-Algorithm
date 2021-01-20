import sys
input = sys.stdin.readline

# 첫째 줄에 블록을 모두 놓았을 때 얻은 점수를 출력
# 둘째 줄에는 파란색 보드와 초록색 보드에서 타일이 들어있는 칸의 개수를 출력

N = int(input())
for _ in range(N):
    t, x, y = map(int, input().split())

