bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

# 성공 코드 - 큐의 길이를 유동적으로 조절함.
def solution(N, W, trucks):
    Q = [0] * N   # 다리 부분

    timer = 0
    while trucks:
        # print(Q)
        if sum(Q[1:]) + trucks[0] <= W:
            Q.append(trucks.pop(0))
        else:
            while Q[1] == 0:
                Q.pop(0)
                Q.append(0)
                timer += 1
            Q.append(0)
        timer += 1
        Q.pop(0)
    timer += len(Q)
    return timer


# tc 한 개 시간 초과로 실패하 코드
# def solution(N, W, trucks):
#     answer = 0
#     Q = [0] * N
#     while Q:
#         answer += 1
#         Q.pop(0)
#         if trucks:
#             if sum(Q) + trucks[0] <= W:
#                 Q.append(trucks.pop(0))
#             else:
#                 Q.append(0)
#     return answer

print(solution(bridge_length, weight, truck_weights))