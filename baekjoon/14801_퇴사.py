import sys
sys.stdin = open('14501_input.txt')

def backtrack(d, money):
    global MAX
    if d >= N:
        if money > MAX:
            MAX = money
        return
    if d + arr[d][0] <= N:
        backtrack(d+arr[d][0], money+arr[d][1])
    backtrack(d+1, money)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

MAX = float('-inf')
backtrack(0, 0)
print(MAX)