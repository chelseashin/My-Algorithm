import sys
sys.stdin = open("14888_input.txt")
input = sys.stdin.readline

# 방법 1
def solve(depth):
    global MIN, MAX
    if depth == N-1:
        result = A[0]
        for j in range(N-1):
            if temp[j] == 0:
                result += A[j+1]
            elif temp[j] == 1:
                result -= A[j+1]
            elif temp[j] == 2:
                result *= A[j+1]
            elif temp[j] == 3:
                result = int(result / A[j+1])
        MIN = min(MIN, result)
        MAX = max(MAX, result)
        return
    for i in range(4):
        if operators[i]:
            operators[i] -= 1
            temp.append(i)
            solve(depth+1)
            temp.pop()
            operators[i] += 1

# 방법 2
# def solve(depth, temp):
#     global MIN, MAX
#     if depth == N:
#         MIN = min(MIN, temp)
#         MAX = max(MAX, temp)
#         return
#     if operators[0]:
#         operators[0] -= 1
#         solve(depth+1, temp+A[depth])
#         operators[0] += 1
#     if operators[1]:
#         operators[1] -= 1
#         solve(depth+1, temp-A[depth])
#         operators[1] += 1
#     if operators[2]:
#         operators[2] -= 1
#         solve(depth+1, temp*A[depth])
#         operators[2] += 1
#     if operators[3]:
#         operators[3] -= 1
#         solve(depth+1, int(temp/A[depth]))
#         operators[3] += 1
# main
N = int(input())
A = list(map(int, input().split()))
operators = list(map(int, input().split()))
MAX = float('-inf')
MIN = float('inf')

# 방법 1
temp = []
solve(0)
# 방법 2
# solve(1, A[0])
print(MAX)
print(MIN)
