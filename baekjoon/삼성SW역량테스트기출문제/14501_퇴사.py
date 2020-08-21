import sys
sys.stdin = open('14501_input.txt')


def solve(day, pay):
    global MAX
    if day >= N:
        MAX = max(MAX, pay)
        return
    if day + schedule[day][0] <= N:
        solve(day+schedule[day][0], pay + schedule[day][1])
    solve(day+1, pay)

# 다른 풀이
# def solve(day, pay):
#     temp = 0
#     if day > N: return 0
#     if day == N:  return pay
#     temp = max(temp, solve(day+schedule[day][0], pay+schedule[day][1]), solve(day+1, pay))
#     return temp

# main
N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
# print(schedule)

MAX = float('-inf')
solve(0, 0)
print(MAX)

# print(solve(0, 0))