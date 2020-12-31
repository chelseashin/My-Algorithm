import sys
sys.stdin = open("14501_input.txt")
input = sys.stdin.readline

# def backtracking(pos, pay):
#     global MAX
#     if pos >= N:
#         MAX = max(MAX, pay)
#         return
#     if pos + A[pos][0] <= N:
#         backtracking(pos + A[pos][0], pay + A[pos][1])
#     backtracking(pos+1, pay)

def backtracking(day, pay):
    temp = 0
    if day > N:
        return 0
    if day == N:
        # print(pay)
        return pay
    temp = max(temp, backtracking(day+A[day][0], pay+A[day][1]), backtracking(day+1, pay))
    return temp

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
print(N, A)
MAX = 0
# backtracking(0, 0)
# print(MAX)
print(backtracking(0, 0))