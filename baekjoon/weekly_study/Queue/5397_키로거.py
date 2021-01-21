import sys
sys.stdin = open("5397_input.txt")

T = int(input())
for tc in range(T):
    data = input()
    # 스택 2개 이용
    left, right = [], []
    for i in data:
        if i == "<":
            if left:
                right.append(left.pop())
        elif i == ">":
            if right:
                left.append(right.pop())
        elif i == "-":
            if left:
                left.pop()
        else:
            left.append(i)
    print(''.join(left + right[::-1]))