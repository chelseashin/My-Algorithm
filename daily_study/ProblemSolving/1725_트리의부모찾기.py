# 16:00 start
# 16:36 pass

from sys import stdin
input = stdin.readline

def solve():
    parentNode = {i: 0 for i in range(1, N+1)}
    parentNode[1] = 1
    stack = [1]
    while stack:
        x = stack.pop()
        for nx in connectInfo[x]:
            if parentNode[nx]:
                continue
            parentNode[nx] = x      # 방문 표시
            stack.append(nx)

    # 출력
    for i in range(2, N+1):
        print(parentNode[i])
    
# main
N = int(input())   # 연결 정보 저장
connectInfo = {i: [] for i in range(1, N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    connectInfo[a].append(b)
    connectInfo[b].append(a)
solve()