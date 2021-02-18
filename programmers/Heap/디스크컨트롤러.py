# 13:05 start
# 13:35 첫 시도 실패..
# 생각보다 변수들이 많이 필요한 것 같다.. 좀더 생각해보자
# 참고 링크 : https://seoyoung2.github.io/algorithm/2020/06/04/Programmers-diskcontroller.html

from heapq import heappop, heappush

# 다른 풀이 1
def solution(jobs):
    cnt, last, answer = 0, -1, 0
    jlen = len(jobs)
    heap = []
    jobs.sort()
    time = jobs[0][0]   # 시작시간 초기화
    while cnt < jlen:
        for s, t in jobs:
            if last < s <= time:
                # 작업 소요시간으로 최소힙 만들기 (t, s)로 push
                heappush(heap, (t, s))
        # 바로 수행할 수 있는 작업이 있는 경우
        if len(heap) > 0:
            cnt += 1
            last = time
            term, start = heappop(heap)
            time += term
            answer += (time - start)
        # 바로 수행할 수 있는 작업이 없는 경우
        else:
            time += 1

    return answer // cnt


# 다른 풀이 2 - Heap 사용한 것보다 압도적으로 빨리 수행됨
# 참고 링크 : https://johnyejin.tistory.com/132
# 아니.. 너무 어렵다 이해하기가.. 역량 부족인 듯
# def solution(jobs):
#     answer = 0
#     start = 0
#     N = len(jobs)
#     jobs.sort(key=lambda x: x[1])
#     print(jobs)
#     while jobs:
#         for i in range(len(jobs)):
#             # 작업 수행할 수 있으면
#             if jobs[i][0] <= start:     # 시작시간 조건
#                 start += jobs[i][1]     # 소요시간 조건
#                 answer += start - jobs[i][0]
#                 jobs.pop(i)
#                 break
#             # 해당 시점에 작업 들어오지 않았으면 시간 += 1
#             if i == len(jobs) - 1:
#                 start += 1
#         print(start, answer, jobs)
#     return answer // N

print(solution([[0, 3], [1, 9], [2, 6]]))               # 9
# print(solution([[0, 3], [4, 3], [10, 3]]))              # 3
# print(solution([[0, 10], [2, 3], [9, 3]]))              # 9
# print(solution([[1, 10], [3, 3], [10, 3]]))             # 9
# print(solution([[0, 10]]))                              # 10
# print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))   # 15
# print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))   # 74
# print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))   # 74