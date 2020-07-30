priorities = [2, 1, 3, 2]
location = 2

# def solution(priorities, location):
#     answer = 0
#     Q = [(idx, value) for idx, value in enumerate(priorities)]
#     # print(sorted(Q, key=lambda x:x[1], reverse=True))
#     # print(Q)
#     while Q:
#         idx, first = Q.pop(0)
#         for temp in Q:
#             if first < temp[1]:
#                 Q.append((idx, first))
#                 break
#         else:
#             if priorities[location] == first:
#                 answer += 1
#         # print(Q)
#     return answer

from collections import deque
def solution(priorities, location):
    from collections import deque
    answer = 0
    Q = deque([(value, idx) for idx, value in enumerate(priorities)])
    while Q:
        item = Q.popleft()
        if Q and item[0] < max(Q)[0]:
            Q.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
        # print(Q)
    return answer


# from collections import deque
# def solution(priorities, location):
#   answer = 0
#   d = deque([(v,i) for i,v in enumerate(priorities)])
#
#   while len(d):
#       item = d.popleft()
#       if d and max(d)[0] > item[0]:
#           d.append(item)
#       else:
#           answer += 1
#           if item[1] == location:
#               break
#   return answer
print(solution(priorities, location))