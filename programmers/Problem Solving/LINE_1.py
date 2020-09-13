boxes = [[1, 2], [2, 3], [3, 1]]


def solution(boxes):
    # answer = -1
    D = dict()
    while boxes:
        a, b = boxes.pop()
        if a not in D:
            D[a] = 1
        else:
            D[a] += 1
        if b not in D:
            D[b] = 1
        else:
            D[b] += 1
    cnt = 0
    for idx, values in D.items():
        if values == 1:
            cnt += 1
    # print(cnt)
    print(D)

    return cnt // 2

print(solution(boxes))