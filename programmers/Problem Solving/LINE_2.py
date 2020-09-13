# ball = [1, 2, 3, 4, 5, 6]
# order = [6, 2, 5, 1, 4, 3]

ball = [11, 2, 9, 13, 24]
order = [9, 2, 13, 24, 11]

def solution(ball, order):
    answer = []
    keep = []
    for num in order:
        if num == ball[0]:
            answer.append(ball.pop(0))
            if ball:
                K = len(keep)
                for _ in range(K):
                    if ball[0] in keep:
                        keep.remove(ball[0])
                        answer.append(ball.pop(0))
        elif num == ball[-1]:
            answer.append(ball.pop())
            if ball:
                K = len(keep)
                for _ in range(K):
                    if ball[-1] in keep:
                        keep.remove(ball[-1])
                        answer.append(ball.pop())
        else:
            keep.append(num)
    return answer

print(solution(ball, order))