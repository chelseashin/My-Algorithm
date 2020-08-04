import sys
sys.stdin = open('16637_input.txt')


def dfs(pos=1):
    global MAX
    if pos >= N:
        print(check)
        return
    check[pos] = 1
    MAX = max(MAX, dfs(pos+4))
    check[pos] = 0
    MAX = max(MAX, dfs(pos+2))
    return MAX

N = int(input())
S = input()
MAX = -2**31
check = [0] * N

print(dfs())
