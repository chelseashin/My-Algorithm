import sys
sys.stdin = open('16637_input.txt')

# 참고 링크 : https://calmlife.tistory.com/18
# 우선순위 없이 계산은 왼쪽부터 순서대로
# 괄호 추가하면 괄호 안의 식 먼저 계산
# 중첩 괄호 불가

# DFS + Backtracking으로 모든 경우를 다 해보는 Brute Force 문제
# 홀수 번째 인덱스는 수식이고 짝수 번째 인덱스는 숫자인 것을 이용
# check 리스트를 이용해서 그 자리에 해당하는 수식이 켜져 있는지 꺼져있는지 확인 후 계산

from collections import deque
input = sys.stdin.readline

def cal2(n1, op, n2):    # 연산 받아서 계산
    if op == '+':
        return n1+n2
    if op == '-':
        return n1-n2
    if op == '*':
        return n1*n2

def calculation():
    Q = deque()
    i = 0
    while True:                 # 괄호 먼저 처리
        if i == N:
            break
        # 수식 자리이고, check 켜져있으면(괄호이면)
        if i % 2 and check[i]:
            # 계산해서 Q에 넣어주기
            Q.append(cal2(int(Q.pop()), S[i], int(S[i+1])))
            # 윗줄에서 계산할때 i+1 썼으니까 i+=1 해줌
            i += 1
        # 수식이 아니거나 안 켜져 있으면 그냥 넣어줌
        else:
            Q.append(S[i])
        i += 1
    # 괄호처리 완료된 수식 처리
    while Q:    # Q에 숫자 하나만 남을 때까지
        if len(Q) == 1:
            break
        # 왼쪽부터 빼면서 계산해주고 다시 왼쪽에 넣어주기
        Q.appendleft(cal2(int(Q.popleft()), Q.popleft(), int(Q.popleft())))
    return Q[0]

# 완전탐색
def solve(pos):
    global result
    if pos >= N:    # n개 이상이면 => 끝에 다다르면 계산해줌
        return calculation()
    # 수식을 선택했으면, 다다음 수식으로(중첩 괄호 불가하기 때문)
    check[pos] = 1
    result = max(result, solve(pos+4))
    # 선택 안 하면, 주어진 문자열에서 2칸 뒤에서 선택 가능
    check[pos] = 0
    result = max(result, solve(pos+2))
    return result

# main
N = int(input())
S = input()
result = float('-inf')
check = [0] * N
print(solve(1))