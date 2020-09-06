import sys
sys.stdin = open('17140_input.txt')

# 시뮬레이션 문제
# 문제를 꼼꼼하게 읽고 조건 빠짐없이 그대로 코딩
# 다음에 풀 때는 같은 로직으로 수행되는 R, C 연산 부분을 함수로 짜보기!

# Counter 모듈 사용
# Counter('리스트명').items()
# 리스트를 구성하는 각 숫자의 등장 횟수를
# 딕셔너리처럼 보여주는 module

# 정렬할 때 다중조건 한번에 해결하기 - 정렬하고 싶은 기준을 순서대로 기입
# sorted(e, key = lambda x : (x[0], -x[1]))
# 아이템 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬하고,
# - 붙이면 내림차순으로 정렬

from collections import Counter


# R 연산과 C 연산 로직이 똑같기 때문에 하나의 함수로 처리
def calculation(A):
    new_A = []  # 새로운 배열 A에 채우기
    max_col = 0
    for row in A:
        new_row = []
        L = Counter(row).items()
        count_table = sorted(L, key=lambda x: (x[1], x[0]))
        for num, cnt in count_table:
            if num == 0:  # 0이면 무시
                continue
            new_row.append(num)
            new_row.append(cnt)
        max_col = max(max_col, len(new_row))
        new_A.append(new_row)
    
    # 가장 긴 열의 길이에 맞춰 0으로 채우기
    for row in new_A:
        if len(row) < max_col:
            row += [0] * (max_col - len(row))
    return new_A

# main
r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

if len(A) > r-1 and len(A[0]) > c-1:
    if A[r-1][c-1] == k:
        print(0)
        exit()

second = 0
while True:
    # 종료 조건 - 찾으면 시간 출력
    if len(A) > r-1 and len(A[0]) > c-1:
        if A[r-1][c-1] == k:
            print(second)
            exit()
    if second > 100:
        print(-1)
        exit()
    second += 1

    # 매 초마다 조건에 따라 R 또는 C 연산을 수행함
    # R 연산
    if len(A) >= len(A[0]):     # 행의 개수 >= 열의 개수일 때
        A = calculation(A)
        continue

    # C 연산
    elif len(A) < len(A[0]):    # 행의 개수 < 열의 개수일 때
        A = list(map(list, zip(*A)))
        new_A = calculation(A)
        A = list(map(list, zip(*new_A)))
        continue