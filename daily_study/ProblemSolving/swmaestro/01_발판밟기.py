n = int(input())
maxCnt = 0
arr = list(map(int, input().split()))
for i in range(n):
    cnt = 0
    visit = [0] * n
    x = i
    while 1:
        visit[x] = 1
        cnt += 1
        nx = x + arr[x]
        if visit[nx]:
            maxCnt = max(maxCnt, cnt+1)
            break
        x = nx
print(maxCnt)