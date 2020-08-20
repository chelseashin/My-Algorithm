N = 8
# N = int(input())
cnt = 0

def func(depth):
    global cnt
    if depth == N:
        cnt += 1
        return
    for i in range(N):
        if visited1[i] or visited2[i+depth] or visited3[depth-i+N-1]:
            continue
        visited1[i] = 1
        visited2[i+depth] = 1
        visited3[depth-i+N-1] = 1
        func(depth+1)
        visited3[depth-i+N-1] = 0
        visited2[i+depth] = 0
        visited1[i] = 0


visited1 = [0] * 40
visited2 = [0] * 40
visited3 = [0] * 40
func(0)
print(cnt)