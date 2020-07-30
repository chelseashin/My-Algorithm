def solution(a, b):
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = b
    for i in range(1, a+1):
        total += months[i]
    answer = days[total%7-1]
    return answer
    # 컴팩트한 한줄 코딩
    # return days[(sum(months[:a-1])+b-1)%7]

a, b = 5, 24
print(solution(a, b))