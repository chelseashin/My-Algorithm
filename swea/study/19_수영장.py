import sys
sys.stdin = open('19_input.txt')

# 보충

def backtrack(n, cost): # n: 현재 달, cost: 이용료
    global ans
    if n >= 13:
        ans = min(ans, cost)
        return
    # 이용일이 없는 경우
    if arr[n] == 0:
        backtrack(n+1, cost)
    # 이용일이 있는 경우
    else:
        # 3가지 선택지
        backtrack(n+1, cost + day * arr[n])
        backtrack(n+1, cost + month)
        backtrack(n+3, cost + quarter)

T = int(input())
for tc in range(T):
    day, month, quarter, year = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    ans = year

    backtrack(1, 0)

    print("#{} {}".format(tc+1, ans))

# TC = int(input())
#
# for tc in range(TC):
# fees = list(map(int, input().split()))
# month = list(map(int, input().split()))
# months = [0] * 12
# for m in range(12):
# months[m] = min(fees[0] * month[m], fees[1])
#
# min_fee = [0] * 12
# min_fee[0] = months[0]
#
# for i in range(1, 12):
# min_fee[i] = min_fee[i - 1] + months[i]
# if i == 2:
# if min_fee[2] > fees[2]:
# min_fee[2] = fees[2]
# if i >= 3:
# if min_fee[i] > min_fee[i - 3] + fees[2]:
# min_fee[i] = min_fee[i - 3] + fees[2]
#
# print(min_fee)
#
# print("#{} {}".format(tc + 1, min(min_fee[11], fees[3])))
