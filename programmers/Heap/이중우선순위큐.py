# 17:00 start
# 17:27 finish

# 이진탐색으로 DP 구현 https://jason9319.tistory.com/113

# Heap을 이용해 개선한 풀이 - heap 한 개만 써서 가장 깔끔하고 직관적
import heapq

# def solution(operations):
#     heap = []
#     for operation in operations:
#         cmd, num = operation.split()
#         if cmd == 'I':
#             heapq.heappush(heap, int(num))
#         elif heap:
#             if num == '1':
#                 # 원소의 remove가 가능한 이유는 힙의 근간이 리스트이기 때문!
#                 heap.remove(max(heap))
#             else:
#                 heapq.heappop(heap)
#     if not heap:
#         return [0, 0]
#     else:
#         return [max(heap), heapq.heappop(heap)]

# 최소 힙, 최대 힙 따로 사용한 코드
# 추가 설명 : 항상 최대힙과 최소힙은 길이가 같으므로
# 최대힙 or 최소힙이 바닥나는 경우는 모든 숫자를 다 썼을때 입니다.
# 하지만, 만약 숫자가 총 4개가 들어갔고 최대힙, 최소힙에 각각 2번의 삭제명령이 있었다면
# 원래 빈 리스트가 되어야 하므로,
# 뒤에 -max_heap[0](2번째로 작았던 수)와 min_heap[0](2번째로 컸던 수)를 비교하는 조건을 추가해 주신 것 같습니다!

def solution(operations):
    max_heap = []
    min_heap = []
    for operation in operations:
        cmd, num = operation.split()
        if cmd == "I":
            heapq.heappush(max_heap, -int(num))
            heapq.heappush(min_heap, int(num))
        else:
            print(cmd, num, "연산 전", min_heap, max_heap)
            if num == "1":  # 최댓값 삭제
                if max_heap:
                    heapq.heappop(max_heap)
                    if not max_heap or -max_heap[0] < min_heap[0]:
                        min_heap, max_heap = [], []
                    print(cmd, num, "최댓값 제거 연산 후", min_heap, max_heap)
            else:           # 최솟값 삭제
                if min_heap:
                    heapq.heappop(min_heap)
                    if not min_heap or -max_heap[0] < min_heap[0]:
                        min_heap, max_heap = [], []
                    print(cmd, num, "최솟값 제거 연산 후", min_heap, max_heap)
    if not min_heap:
        return [0, 0]
    return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]

# 처음 풀이
# Heap 안 쓰고 List로 개떡같이 짰는데 TC가 적어서인지 통과됨..
# def solution(operations):
#     Q = []
#     for operation in operations:
#         cmd, num = operation.split()
#         if cmd == 'I':
#             Q.append(int(num))
#         else:
#             Q.sort()
#             if Q:
#                 if num == '1':
#                     Q.pop()
#                 else:
#                     Q.pop(0)
#     if not Q:
#         return [0, 0]
#     return [max(Q), min(Q)]

# print(solution(["I 16", "D 1"]))
# print(solution(["I 7", "I 5", "I -5", "D -1"]))
# print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))