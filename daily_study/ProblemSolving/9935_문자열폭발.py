from sys import stdin
input = stdin.readline

def solve():
    blen = len(bomb_temp)       # 폭발 문자열의 길이
    last_bomb = bomb_temp[-1]   # 폭발 문자열의 마지막 글자
    stack = []
    for char in temp:
        stack.append(char)
        if char == last_bomb and bomb_temp == stack[-blen:]:
            for _ in range(blen):   # 길이만큼 stack의 문자 삭제
                stack.pop()
            # print("stack", stack)

    result = ''.join(stack)
    if result:
        return result
    else:
        return "FRULA"

# main
temp = input().strip()                # 전체 문자열
bomb_temp = list(input().strip())     # 폭발 문자열
print(solve())