m = "kkaxbycyz"
k = "abc"

def solution(m, k):
    answer = ''
    idx = 0
    for i in range(len(m)):
        if m[i] == k[idx]:
            idx += 1
            if idx == len(k):
                answer += m[i+1:]
                break
        else:
            answer += m[i]
    return answer

print(solution(m, k))