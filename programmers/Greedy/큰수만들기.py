number = "4177252841"
k = 4

# 성공 - 자릿수 Stack에 넣어가며 채워가기
def solution(number, k):
    stack = []
    for num in number:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k > 0:
        stack = stack[:-1]
    # print(stack)
    return ''.join(stack)

print(solution(number, k))