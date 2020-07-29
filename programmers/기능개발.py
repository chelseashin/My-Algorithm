progresses = [93, 30, 55]
speeds = [1, 30, 5]

from math import ceil

def solution(progresses, speeds):
    answer = []
    days = [ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    # print(days)
    front = 0
    for idx in range(len(days)):
        if days[front] < days[idx]:
            answer.append(idx-front)
            front = idx
    answer.append(len(days)-front)
    return answer

print(solution(progresses, speeds))