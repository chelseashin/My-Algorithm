# 분할정복

# def divide(array, x):
#     n1 = max(array[:x])
#     n2 = max(array[x:])
#
#     if n1 > n2:
#         return n1, array[x:]
#     else:
#         return n2, array[:x]
#
# def main():
#     n = int(input())
#     array = list(map(int, input().split()))
#     answer = 0
#     while True:
#         num, new_array = divide(array, n//2)
#         if len(new_array) == 1:
#             answer += num
#             break
#         answer += num
#         n //= 2
#         array = new_array
#     print(answer)

def solve(start, end, arr):
    if end - start == 1:
        return max(arr[start], arr[end])
    res = 0
    mid = (start + end) // 2
    leftMax = max(arr[start:mid+1])
    rightMax = max(arr[mid+1:end+1])
    # 왼쪽 선택
    res = max(res, solve(start, mid, arr) + rightMax)
    # 오른쪽 선택
    res = max(res, solve(mid+1, end, arr) + leftMax)
    return res


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(0, n-1, arr))

if __name__ == "__main__":
    main()