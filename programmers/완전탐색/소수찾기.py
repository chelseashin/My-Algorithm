from itertools import permutations
def solution(numbers):
    answer = 0

    # 가능한 수의 조합 만들기
    lst = ','.join(numbers).split(',')
    # print(lst)
    possible = []

    for i in range(len(numbers)):
        possible.extend(list(permutations(lst, i+1)))

    possible = [''.join(i) for i in possible]
    possible = sorted(list(set(map(int, possible))))

    # print(possible)
    idx = -1
    for i in range(len(possible)):
        if possible[i] <= 1: idx = i
        else: break

    if idx == -1: pass
    else: possible = possible[idx+1:]

    # 소수 찾아내기
    for num in possible:
        for i in range(2, round(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            answer += 1

    return len(possible)

print(solution('17'))