from itertools import combinations

def solution(orders, course):
    D = dict()
    for order in orders:
        for c in course:
            if c <= len(order):
                for comb in combinations(order, c):
                    temp = ""
                    for menu in sorted(comb):
                        temp += menu
                    if temp not in D:
                        D[temp] = 1
                    else:
                        D[temp] += 1

    result = sorted(D.items(), key=lambda x: x[1], reverse=True)
    # print('result', result)
    answer = []

    num = []
    for name, cnt in result:
        if cnt < 2:
            break
        # 값 없으면 등록해주고
        if cnt not in num:
            answer.append((name, cnt))
            num.append(cnt)
        # 값 있으면
        else:
            max_name, max_cnt = answer[-1]
            if len(name) > len(max_name) and cnt == max_cnt:
                answer[-1] = (name, cnt)

    for name, cnt in result:
        for a, c in answer:
            if len(name) == len(a) and cnt == c and (name, cnt) not in answer:
                answer.append((name, cnt))

    # print(num)
    # print(answer)
    ans = []
    for A in sorted(answer):
        ans.append(A[0])
    return ans


orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
print(solution(orders, course))