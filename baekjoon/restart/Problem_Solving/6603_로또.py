import sys
sys.stdin = open('6603_input.txt')

def dfs(depth, k):
    global order
    if depth == 6:
        for o in order:
            print(line[o], end=' ')
        print()
        return
    for i in range(k, N):
        order.append(i)
        dfs(depth+1, i+1)
        order.pop()

while True:
    line = list(map(int, input().split()))
    N = line.pop(0)
    if N == 0:
        break
    # print(line)
    order = []
    dfs(0, 0)
    print()


# tool 사용
# from itertools import combinations
#
# while True:
#     line = list(map(int, input().split()))
#     N = line.pop(0)
#     for comb in list(combinations(range(N), 6)):
#         for c in comb:
#             print(line[c], end=' ')
#         print()
#     print()
#     if N == 0:
#         break