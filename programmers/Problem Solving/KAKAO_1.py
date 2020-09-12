new_id = "...!@BaT#*..y.abcdefghijklm"

def solution(new_id):
    answer = ""
    # 1, 2단계
    for n in new_id.lower():
        if n.isalpha() or n.isdigit():
            answer += n
        elif n == "-" or n == "_" or n == ".":
            answer += n
    # 3단계
    third = answer[0]
    for i in range(1, len(answer)):
        if answer[i-1] == "." and answer[i] == answer[i-1]:
            continue
        third += answer[i]
    # 4단계
    if third[0] == ".":
        third = third[1:]
    if len(third) and third[-1] == ".":
        third = third[:-1]
    # 5단계
    if not len(third):
        third = "a"
    # 6단계
    if len(third) > 15:
        third = third[:15]
    if third[-1] == "." and len(third) > 1:
        third = third[:-1]
    # 7단계
    if len(third) <= 2:
        temp = third[-1]
        for _ in range(3 - len(third)):
            third += temp
    return third

# print(solution(new_id))
ids = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=",
       "123_.def", "abcdefghijklmn.p"]
for new_id in ids:
    print(solution(new_id))