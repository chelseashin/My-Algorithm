numbers = [1, 1, 1, 1, 1]
target = 3

def solution(numbers, target):
    global answer
    answer = 0
    order = []
    dfs(0, 0, numbers, target, order)
    return answer

def dfs(depth, k, numbers, target, order):
    global answer
    N = len(numbers)
    if depth == N:
        # print(order)
        temp = 0
        for j in range(N):
            temp += order[j] * numbers[j]
        if temp == target:
            answer += 1
        return
    for i in [-1, 1]:
        order.append(i)
        dfs(depth+1, i, numbers, target, order)
        order.pop()

print(solution(numbers, target))