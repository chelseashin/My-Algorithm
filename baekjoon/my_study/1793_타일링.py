import sys
sys.stdin = open("1793_input.txt")
input = sys.stdin.readline
def solve(N):
    if N == 0 or N == 1:
        return 1
    a = [0] * (N+1)
    a[0], a[1] = 1, 1
    for i in range(2, N+1):
        a[i] = a[i-1] + 2 * a[i-2]
    return a[N]

while True:
    try:
        print(solve(int(input())))
    except:
        break