L = [3, 4, 6, 4, 3, 7, 2]   # 4, 2

def ascending(arr):
    now = arr[0]
    result = 1
    for i in range(1, len(arr)):
        if now < arr[i]:
            result += 1
            now = arr[i]
    return result

N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

print(ascending(A))
A.reverse()
print(ascending(A))