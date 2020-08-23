import sys
sys.stdin = open('14888_input.txt')

def solve(depth, result):
    global MIN, MAX
    if depth == len(num):
        MAX = max(MAX, result)
        MIN = min(MIN, result)
        return
    if operators[0]:
        operators[0] -= 1
        solve(depth+1, result+num[depth])
        operators[0] += 1
    if operators[1]:
        operators[1] -= 1
        solve(depth+1, result-num[depth])
        operators[1] += 1
    if operators[2]:
        operators[2] -= 1
        solve(depth+1, result*num[depth])
        operators[2] += 1
    if operators[3]:
        operators[3] -= 1
        solve(depth+1, int(result/num[depth]))
        operators[3] += 1

# main
N = int(input())
num = list(map(int, input().split()))
operators = list(map(int, input().split()))
S = sum(operators)
MAX = float('-inf')
MIN = float('inf')

solve(1, num[0])
print(MAX)
print(MIN)