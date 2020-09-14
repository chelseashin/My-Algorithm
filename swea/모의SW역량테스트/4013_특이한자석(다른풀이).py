import sys
sys.stdin = open('4013_input.txt')

# main
T = int(input())
for tc in range(T):
    K = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]

    for _ in range(K):
        num, dir = map(int, input().split())
        checked = [0] * 4       # 회전방향 저장
        checked[num-1] = dir
        # 오른쪽
        for i in range(num-1, 3):
            if mag[i][2] != mag[i+1][6]:
                checked[i+1] = -checked[i]
            else:
                break
        # 왼쪽
        for i in range(num-1, 0, -1):
            if mag[i-1][2] != mag[i][6]:
                checked[i-1] = -checked[i]
            else:
                break
        # print(checked)
        # 회전
        for i in range(4):
            if checked[i] == 1:
                mag[i] = [mag[i][-1]] + mag[i][:-1]
            elif checked[i] == -1:
                mag[i] = mag[i][1:] + [mag[i][0]]

    answer = 0
    for i in range(4):
        if mag[i][0]:
            answer += (1 << i)
    print("#{} {}".format(tc+1, answer))