s = "ababcdcdababcdcd"


# def solution(s):
#     length = []
#     result = ""
#     N = len(s)
#
#     if N == 1:
#         return 1
#
#     for cut in range(1, N // 2 + 1):
#         count = 1
#         tempStr = s[:cut]
#         for i in range(cut, len(s), cut):
#             if s[i:i + cut] == tempStr:
#                 count += 1
#             else:
#                 if count == 1:
#                     count = ""
#                 result += str(count) + tempStr
#                 tempStr = s[i:i + cut]
#                 count = 1
#         print(result)
#         if count == 1:
#             count = ""
#         result += str(count) + tempStr
#         print(result)
#         length.append(len(result))
#         result = ""
#
#     return min(length)

def solution(string):
    N = len(string)
    answer = float('inf')
    if N == 1:
        return 1
    # 몇 단위로 할 것인지 1에서 N//2 + 1사이로 돌려보기
    for end in range(1, N // 2 + 1):
        res = ''
        cnt = 1
        temp_str = string[:end]
        for i in range(end, N+end, end):
            if temp_str == string[i:i+end]:
                cnt += 1
            else:
                if cnt != 1:
                    res += str(cnt) + temp_str
                else:
                    res += temp_str
                temp_str = string[i:i+end]
                cnt = 1
        # print(res, len(res))
        answer = min(answer, len(res))

    return answer

print(solution(s))


# tc 넣어보기
a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",
    'aaaaaa',
]

for x in a:
    print(solution(x))