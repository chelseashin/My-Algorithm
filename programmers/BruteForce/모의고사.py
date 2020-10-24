def solution(answers):
    pattern = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    L = [0] * 3
    for i, ans in enumerate(answers):
        if ans == pattern[0][i%5]:
            L[0] += 1
        if ans == pattern[1][i%8]:
            L[1] += 1
        if ans == pattern[2][i%10]:
            L[2] += 1
    MAX = max(L)
    answers = [i+1 for i in range(len(L)) if L[i] == MAX]
    return answers

print(solution([1, 2, 3, 4, 5]))