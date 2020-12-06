import sys
sys.stdin = open("5076_input.txt")

while True:
    code = input()
    if code == "#":
        break
    result = "legal"
    stack = []
    # print(code)
    idx = 0
    for i in range(len(code)):
        if code[i] == "<":
            idx = i + 1
            temp = "<"
            # for j in range(idx)
            while True:
                temp += code[idx]
                idx += 1
                if code[idx] == ">":
                    temp += ">"
                    break
            print(temp)
            if not stack:
                stack.append(temp)
    break