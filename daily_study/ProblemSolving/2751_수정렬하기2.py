# Merge Sort로 풀기
# 병합정렬은 분할정복 알고리즘의 대표적인 예
# 시간복잡도 O(NlogN)을 보장
# 나눌 수 없을 때까지 나누고 병합하는 과정 재귀로 반복


def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            if left[i] < right[j]:
                a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
    return a

N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
A = merge_sort(A)   # 병합 정렬
for data in A:
    print(data)