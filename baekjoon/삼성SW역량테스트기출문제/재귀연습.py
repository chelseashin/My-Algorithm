def solve(pos, score):
    res = 0
    if pos == 3:
        print('score return:', score)
        return score
    res = max(res, solve(pos+1, score+a[pos]))    # 선택했을 때
    res = max(res, solve(pos+1, score))           # 선택하지 않았을 때
    print('res return:', res)
    return res

a = [1, 2, 3]
# solve(0, 0)
print(solve(0, 0))

print(max(1e9, 1))