from itertools import combinations

import sys
sys.stdin = open('2798_input.txt')

def dfs(depth, k):
    global N, M, diff, ans
    if depth == 3:
        temp = cards[order[0]] + cards[order[1]] + cards[order[2]]
        # print(temp)
        if temp <= M:
            if M-temp < diff:
                diff = M-temp
                ans = temp
        return

    for i in range(k, N):
        if visited[i]:
            continue
        visited[i] = 1
        order.append(i)
        dfs(depth+1, i)
        order.pop()
        visited[i] = 0

N, M = map(int, input().split())
cards = list(map(int, input().split()))
diff = float('inf')
ans = 0
order = []
visited = [0] * N
dfs(0, 0)
print(ans)

# print(cards)
# itertools 사용 풀이(성공)
# diff = float('inf')
# for comb in list(combinations(range(N), 3)):
#     temp = 0
#     for c in comb:
#         temp += cards[c]
#     if temp <= M:
#         if M-temp < diff:
#             diff = M-temp
#             ans = temp
# print(ans)