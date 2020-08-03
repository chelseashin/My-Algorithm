name = 'JEROEN'

def solution(name):
    answer = 0
    name = list(name)
    N = len(name)
    raw = ['A'] * N
    idx = 0
    while True:
        right_idx = 1
        left_idx = 1
        if name[idx] != 'A':
            if ord(name[idx]) - ord("A") > 13:
                answer += 26-((ord(name[idx])) - ord("A"))
            else:
                answer += ord(name[idx]) - ord("A")
            name[idx] = "A"
        if name == raw:
            break
        else:
            for i in range(1, N):
                if name[idx+1] == "A":
                    right_idx += 1
                else:
                    break
                if name[idx-i] == "A":
                    left_idx += 1
                else:
                    break
            if right_idx > left_idx:
                answer += left_idx
                idx -= left_idx
            else:
                answer += right_idx
                idx += right_idx
    return answer

print(solution(name))