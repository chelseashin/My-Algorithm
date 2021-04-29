from sys import stdin
input = stdin.readline

def solve(numbers):
    print("초기상태", numbers, len(numbers))
    rcnt, dcnt = 0, 0
    for cmd in p:
        if cmd == "R":
            rcnt += 1
        elif cmd == "D":
            try:
                if rcnt % 2 == 0:
                    dcnt += 1    # 나중에 빼줄 때 사용
                else:
                    numbers.pop()         # 지금 바로 빼주기
            except:
                return "error"
    # print("rcnt", rcnt, "dcnt", dcnt, numbers)
    if len(numbers) < dcnt:
        return "error"
    if rcnt%2:
        numbers[dcnt:].reverse()
    else:
        numbers = numbers[dcnt:]
    result = "["
    for i in range(len(numbers)):
        if i < len(numbers)-1:
            result += numbers[i] + ","
        else:
            result += numbers[i] + "]"
    # print("최종", numbers, result)
    return result

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    numbers = input().strip().split(',')
    numbers[0] = numbers[0][1:]
    numbers[-1] = numbers[-1][:-1]
    print(solve(numbers))