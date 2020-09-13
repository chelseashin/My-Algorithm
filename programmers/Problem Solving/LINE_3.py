n = 10007

def dfs(N, depth, min_cnt, result, MIN, temp):
    if depth > min_cnt:
        return
    if len(N) == 1 and depth < min_cnt:
        MIN = min(min_cnt, depth)
        result = int(N)
        return [MIN, int(result)]
    for i in range(1, len(N)):
        if N[i-1] == 0:
            # depth += 1
            pass
        else:
            S = int(N[:i]) + int(N[i:])
        dfs(str(S), depth+1, min_cnt, result, MIN, temp)
    return [min_cnt, result]

def solution(n):
    N = str(n)
    MIN, temp = float('inf'), 0
    answer = dfs(N, 0, float('inf'), 0, MIN, temp)
    return answer

print(solution(n))