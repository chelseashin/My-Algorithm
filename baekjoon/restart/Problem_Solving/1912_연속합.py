import sys
sys.stdin = open('1912_input.txt')

# 슬라이딩 윈도우 방식
# 마치 창문을 한쪽으로 밀면서 문제를 푸는 것과 모양새가 유사해서 붙여진 이름
# 일정 범위를 가지고 있는 것을 유지하면서 이를 이동하며 원하는 값을 찾는 것.
# 투 포인터처럼 구간을 훑으면서 지나간다는 공통점이 있으나,
# 슬라이딩 윈도우는 어느 순간에도 그 구간의 넓이가 동일하다는 차이점이 있다

N = int(input())
L = list(map(int, input().split()))
print(L)
temp = [L[0]]   # 새로운 리스트, 비교를 위해 첫 값 넣어줌
for i in range(N-1):
    # temp의 i번째 인덱스와 L의 i+1번째 인덱스의 숫자를 합한 값과
    # L의 i+1번째 숫자를 비교하여 더 큰 숫자를 temp 리스트에 넣어준다.
    temp.append(max(temp[i]+L[i+1], L[i+1]))
    
print(temp)
print(max(temp))