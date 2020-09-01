import sys
sys.stdin = open('19_input.txt')

# 보충

def backtrack(n, cost): # n: 현재 달, cost: 이용료
    global ans
    if n >= 13:
        ans = min(ans, cost)
        return
    # 이용일이 없는 경우
    if arr[n] == 0:
        backtrack(n+1, cost)
    # 이용일이 있는 경우
    else:
        # 3가지 선택지
        backtrack(n+1, cost + day * arr[n])
        backtrack(n+1, cost + month)
        backtrack(n+3, cost + quarter)

T = int(input())
for tc in range(T):
    day, month, quarter, year = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    ans = year

    backtrack(1, 0)

    print("#{} {}".format(tc+1, ans))