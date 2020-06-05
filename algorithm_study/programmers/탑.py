heights = [5, 3, 1, 2, 3]

def solution(heights):
    H = len(heights)
    answer = [0] * H
    for i in range(H-1, 0, -1):
        for j in range(i-1, -1, -1):
            if heights[j] > heights[i]:
                answer[i] = j+1
                break
    return answer

print(solution(heights))

for s in range(9, 0, -1):
    print(s, end="")