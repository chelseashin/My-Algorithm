# 선택정렬로 풀이
import sys
input = sys.stdin.readline

def selectionSort(A):
    for i in range(N):
        min_idx = i
        for j in range(i + 1, N):
            if A[min_idx] > A[j]:
                min_idx = j  # 최소값 가진 인덱스 저장
        A[i], A[min_idx] = A[min_idx], A[i]  # swap

def bubbleSort(data):
    for i in range(len(data)-1, 0, -1):
        for j in range(0, i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

# selectionSort(A)
# for a in A:
#     print(a)

bubbleSort(A)
for a in A:
    print(a)