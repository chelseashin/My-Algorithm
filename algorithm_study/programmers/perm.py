import sys
import itertools

sys.stdin = open("input.txt")

def solution(numbers):
    global answer
    numbers = sorted(numbers, reverse=True, key=lambda  x: (str(x)*4).ljust(4))
    print(numbers)
    for i in numbers:
        answer += str(i)
    if answer[0] == '0':    #모두 0인 경우 -> 테스트11
        return '0'
    return answer

numbers = list(map(int, input().split()))
N = len(numbers)
answer = ''
solution(numbers)
print(answer)
# for perm in list(itertools.permutations(numbers, N)):
#     print(perm)
