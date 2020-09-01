import sys
sys.stdin = open('1952_input.txt')

# pos: 현재 달, cost: 이용료
def dfs(pos, cost):
    global MIN
    if pos >= 13:
        MIN = min(MIN, cost)
        return
    # 현재 달에 이용일이 없을 경우 다음 달로 넘어감
    if plan[pos] == 0:
        dfs(pos+1, cost)
    # 현재 달에 이용일이 있는 경우
    else:
        # 3가지 선택지
        dfs(pos+1, cost + day * plan[pos])
        dfs(pos+1, cost + month)
        dfs(pos+3, cost + quarter)

T = int(input())
for tc in range(T):
    day, month, quarter, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    MIN = year

    dfs(1, 0)
    print("#{} {}".format(tc+1, MIN))