blocks = [[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]

def solution(blocks):
    answer = []
    extemp = []
    for i in range(len(blocks)):
        temp = [0] * (i + 1)
        temp[blocks[i][0]] = blocks[i][1]

        # 왼쪽 포문
        for left in range(blocks[i][0], 0, -1):
            temp[left - 1] = extemp[left - 1] - temp[left]

        # 오른쪽 포문
        for right in range(blocks[i][0], i):
            temp[right + 1] = extemp[right] - temp[right]

        answer += temp
        extemp = temp

    return answer

print(solution(blocks))