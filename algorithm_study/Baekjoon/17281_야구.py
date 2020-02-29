import sys
sys.stdin = open("17281_input.txt")

def perm(depth):
    if depth == 9:
        print(order)
        return
    if depth == 3:
        order.append(0)
        perm(depth + 1)
        order.pop()
    else:
        for i in range(1, 9):
            if visited[i]:
                continue
            visited[i] = 1
            order.append(i)
            perm(depth+1)
            order.pop()
            visited[i] = 0

N = int(input())
for _ in range(N):
    result = list(map(int, input().split()))
    # print(result)

visited = [0] * 9
order = []
perm(0)
