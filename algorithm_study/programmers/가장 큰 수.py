import sys
sys.stdin = open("input.txt")

def perm(depth):
    global MAX
    if depth == N:
        n = ''
        for o in order:
            n += str(o)
        # print(n)
        if int(n) > MAX:
            MAX = int(n)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            order.append(numbers[i])
            perm(depth+1)
            order.pop()
            visited[i] = 0




numbers = list(map(int, input().split()))
N = len(numbers)
MAX = 0
order = []
visited = [0] * (N+1)
perm(0)
print(MAX)