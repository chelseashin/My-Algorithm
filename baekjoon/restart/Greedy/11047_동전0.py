import sys
sys.stdin = open('11047_input.txt')

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse = True)
ans = 0
for i in range(N):
    if K // coins[i] > 0:
        ans += K // coins[i]
        K -= coins[i] * (K // coins[i])
print(ans)