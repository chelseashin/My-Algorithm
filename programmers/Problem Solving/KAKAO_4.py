n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

def dfs(start, cnt):

def solution(n, s, a, b, fares):
    answer = 0
    A = [[0] * n for _ in range(n)]
    for c, d, f in fares:
        A[c-1][d-1] = f
        A[d-1][c-1] = f
    # for a in A:
    #     print(a)
    dfs(s, a, b, 0)
    return answer

print(solution(n, s, a, b, fares))