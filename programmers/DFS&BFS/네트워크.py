n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

def dfs(start, computers, visited, n):
    for i in range(n):
        if visited[i]:
            continue
        if computers[start][i]:
            visited[i] = 1
            dfs(i, computers, visited, n)

def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(i, computers, visited, n)
        answer += 1
    return answer

print(solution(n, computers))