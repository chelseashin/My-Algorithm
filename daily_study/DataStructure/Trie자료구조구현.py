# https://alpyrithm.tistory.com/74 참고

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    # 문자열 삽입
    def insert(self, string):
        curNode = self.head
        # 삽입할 string 각각의 문자에 대해 자식 Node를 만들며 내려간다.
        for char in string:
            # 자식 Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curNode.children:
                curNode.children[char] = Node(char)
            # 같은 문자가 있으면 해당 노드로 이동
            curNode = curNode.children[char]
        curNode.data = string

    # 문자열이 존재하는지 탐색
    def search(self, string):
        curNode = self.head

        for char in string:
            if char in curNode.children:
                curNode = curNode.children[char]
            else:
                return False
        
        if curNode.data != None:
            return True

# main
N, M = map(int, input().split())
wordTrie = Trie()
lenWord = [False] * 501     # 주어진 문자열과 길이가 같은 문자열에 대해서만 탐색 진행

for _ in range(N):
    word = input().strip()
    wordTrie.insert(word)   # 트라이에 단어 삽입
    lenWord[len(word)] = True
# print("wordTrie 객체로 존재", wordTrie)

result = 0
for _ in range(M):
    word = input().strip()
    if not lenWord[len(word)]:   # 문자열 길이 다르면 탐색 X
        continue
    if wordTrie.search(word):    # 문자열 길이 같으면 탐색 O
        result += 1
print(result)