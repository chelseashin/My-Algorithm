import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)    # 재귀 깊어지는 경우 오류 방지

def dfs(x, cycle):
    global ans
    visited[x] = 1
    cycle.append(x)     # 사이클 이루는지 확인하기 위함
    nx = numbers[x]     # 현재 번호가 가리키는 다음 번호

    if visited[nx]:
        if nx in cycle:     # 사이클 이룸
            # 사이클 이루는 부분의 갯수 전체 갯수에서 빼줌
            ans -= len(cycle) - cycle.index(nx)
            return
    else:
        dfs(nx, cycle)

T = int(input())
for _ in range(T):
    n = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    ans = n
    for i in range(1, n+1):     # 차례대로 확인하며
        if not visited[i]:      # 방문하지 않은 곳이라면 dfs로 사이클 만들기
            dfs(i, [])
    print(ans)