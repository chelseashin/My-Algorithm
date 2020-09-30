import sys
sys.stdin = open('17406_input.txt')


def perm(depth):
    global cal
    if depth == K:
        for j in order:
            print(cal[j])
        print()
    for i in range(K):
        if visit[i]:
            continue
        visit[i] = 1
        order.append(i)
        perm(depth+1)
        order.pop()
        visit[i] = 0

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

cal = []
for _ in range(K):
    cal.append(list(map(int, input().split())))
print(cal)

result = float('-inf')
order = []
visit = [0] * K
perm(0)
print(result)