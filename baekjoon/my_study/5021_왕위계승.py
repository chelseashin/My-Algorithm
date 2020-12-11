import sys
sys.stdin = open('5021_input.txt')

N, M = map(int, input().split())
first = input()
print(N, M, first)
for _ in range(N):
    family = list(input().split())
    print(family)

for _ in range(M):
    name = input()
    print(name)

dfs(first)