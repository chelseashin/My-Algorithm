# 고급 탐색 알고리즘

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회
def pre_order(node):
    print(node.data, end='')            # 시작 위치에서 출력
    if node.left_node != '.':
        pre_order(tree[node.left_node])     # 재귀
    if node.right_node != '.':
        pre_order(tree[node.right_node])

# 중위 순회
def in_order(node):
    if node.left_node != '.':
        in_order(tree[node.left_node])
    print(node.data, end='')            # 중간 위치에서 출력
    if node.right_node != '.':
        in_order(tree[node.right_node])

# 후위 순회
def post_order(node):
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.data, end='')            # 마지막 위치에서 출력

N = int(input())
tree = {}
for i in range(N):
    data, left_node, right_node = input().split()
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])    # 전위순회
print()
in_order(tree['A'])     # 중위순회
print()
post_order(tree['A'])   # 후위순회