# import sys
# input = sys.stdin.readline
# K = int(input())
# A = list(input().split())

# Backtracking + Brute Force

K = 2
A = ["<", ">"]

# 문자열도 부등호로 크기 비교 가능
def check(n1, n2, k):
    if k == '<':
        return n1 < n2
    if k == '>':
        return n1 > n2

def dfs(depth, s):
    global MIN, MAX
    if depth == K+1:    # 종료 조건
        # 정답의 최솟값은 처음 호출된 값, 최댓값은 마지막에 호출된 값
        if MIN == float('inf'):
            MIN = s
        else:
            MAX = s
        return
    for i in range(10):
        if visited[i]:
            continue
        # 재귀 함수를 호출하기 전에, 다음 숫자가 부등식에 맞는지 확인
        if depth == 0 or check(s[-1], str(i), A[depth-1]):
            visited[i] = 1
            dfs(depth+1, s+str(i))
            visited[i] = 0

visited = [0] * 10
MAX = float('-inf')
MIN = float('inf')
dfs(0, '')

print(MAX)
print(MIN)