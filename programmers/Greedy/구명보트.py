people = [70, 50, 80, 50]
limit = 100

# 성공 1 - 두 개를 한꺼번에 태울 수 있는 경우를 전체 갯수에서 빼주기
# def solution(people, limit):
#     answer = 0
#     people.sort()
#     N = len(people)
#     light = 0
#     heavy = N-1
#     while light < heavy:
#         if people[light] + people[heavy] <= limit:
#             answer += 1
#             light += 1
#             heavy -= 1
#         else:
#             heavy -= 1
#     return N - answer

# 성공 2 - 전체 경우가 돌 때마다 +1 해주기
def solution(people, limit):
    answer = 0
    people.sort()
    light = 0
    heavy = len(people)-1
    while light <= heavy:
        answer += 1
        if people[light] + people[heavy] <= limit:
            light += 1
        heavy -= 1
    return answer

print(solution(people, limit))