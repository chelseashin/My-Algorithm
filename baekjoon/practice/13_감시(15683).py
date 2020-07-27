import sys
sys.stdin = open('13_input.txt')

def dfs(depth):
    global arr, kind, count, result
    if depth == count:
        print(result)
        return

    if kind[depth] == 1:
        for i in range(1, 5):
            result.append(i)
            dfs(depth+1)
            result.pop()
    elif kind[depth] == 2:
        for i in range(5, 7):
            result.append(i)
            dfs(depth+1)
            result.pop()
    elif kind[depth] == 3:
        for i in range(7, 11):
            result.append(i)
            dfs(depth + 1)
            result.pop()
    elif kind[depth] == 4:
        for i in range(12, 15):
            result.append(i)
            dfs(depth + 1)
            result.pop()
    elif kind[depth] == 5:
        for i in range(15, 16):
            result.append(i)
            dfs(depth + 1)
            result.pop()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

kind = []
count = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and arr[i][j] != 6:
            kind.append(arr[i][j])
            count += 1

# print(count, kind)

result = []
dfs(0)