# 자연수 N의 범위(3 <= N <= 9)가 매우 한정적이므로 완전탐색으로 문제 해결
# 수의 리스트와 연산자 리스트를 분리하여 모든 경우의 수를 계산(재귀함수 이용)
# 파이썬의 eval() 함수를 이용하여 문자열 형태의 표현식을 계산할 수 있다.

import copy

def solve(arr, n):
    if len(arr) == n:
        # 가능한 모든 경우 연산자 리스트에 담기
        opLSt.append(copy.deepcopy(arr))
        return
    arr.append(' ')
    solve(arr, n)
    arr.pop()

    arr.append('+')
    solve(arr, n)
    arr.pop()

    arr.append('-')
    solve(arr, n)
    arr.pop()

T = int(input())
for _ in range(T):
    N = int(input())

    opLSt = []
    solve([], N-1)
    numLst = [i for i in range(1, N + 1)]
    for op in opLSt:
        temp = ""
        for i in range(N-1):
            temp += str(numLst[i]) + op[i]
        temp += str(numLst[-1])
        if eval(temp.replace(" ", "")) == 0:    # 계산 결과가 0이라면
            print(temp)
    print()