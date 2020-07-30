def solution(arr):
    answer = [arr[0]]
    for i in arr[1:]:
        if i == answer[-1]:
            continue
        answer.append(i)

    return answer
#
arr = [1,1,3,3,0,1,1]
print(solution(arr))

# 다른 풀이
# def no_continuous(s):
#     a = []
#     for i in s:
#         if a[-1:] == [i]: continue
#         a.append(i)
#     return a
#
# print(no_continuous(arr))