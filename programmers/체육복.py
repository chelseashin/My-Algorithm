# 성공 풀이
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for i in _reserve:
        if i-1 in _lost:
            _lost.remove(i-1)
        elif i+1 in _lost:
            _lost.remove(i+1)
    return n-len(_lost)

# set 사용
# def solution(n, lost, reserve):
#     set_reserve = set(reserve) - set(lost)
#     set_lost = set(lost) - set(reserve)
#     for i in set_reserve:
#         if i-1 in set_lost:
#             set_lost.remove(i-1)
#         elif i+1 in set_lost:
#             set_lost.remove(i+1)
#     return n-len(set_lost)


n = 100
lost = [3, 6, 95, 100]
reserve = [2, 5, 5, 5, 50, 50]

print(solution(n, lost, reserve))