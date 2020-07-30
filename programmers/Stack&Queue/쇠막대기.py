arrangement = "()(((()())(())()))(())"

def solution(arrangement):
    answer = 0
    A = arrangement.replace('()', 'P')
    stack = []
    for i in A:
        if i == '(':
            stack.append(i)
            answer += 1
        elif i == ')':
            stack.pop()
        else:
            answer += len(stack)
    return answer

# 다른 풀이 - Stack 안 쓰고 그때 상태의 합을 answer에 더하는 방식
# def solution(arrangement):
#     answer = 0
#     sticks = 0
#     rasor_to_zero = arrangement.replace('()','0')
#
#     for i in rasor_to_zero:
#         if i == '(':
#             sticks += 1
#         elif i =='0' :
#             answer += sticks
#         else :
#             sticks -= 1
#             answer += 1
#
#     return answer

print(solution(arrangement))

