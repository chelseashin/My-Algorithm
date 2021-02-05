# 난이도 중상..
# 알고리즘 : 트리 구현
# 이진트리 입력으로 주어질 때,
# 너비가 가장 넓은 레벨과 그 레벨의 너비를 출력하는 것이 문제!
# 동일한 레벨에서 
# 중위순회를 이용하면 X축을 기준으로 왼쪽부터 방문한다는 특징이 있음.
# 이 문제는 '중위 순회 알고리즘'을 이용하고,
# 추가적으로 Level 값을 저장하도록 하여 문제를 해결할 수 있음.


import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    data, left_node, right_node = map(int, input().split())
    print(data, left_node, right_node)