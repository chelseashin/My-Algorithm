# 참고 링크 : https://dirmathfl.tistory.com/176
# 66%에서 틀림

from sys import stdin
input = stdin.readline

def dfs(depth, pos):
    global answer
    if depth == K-5:    # 새로 배워야할 알파벳 수에 다다랐을 때
        readCnt = 0     # 읽을 수 있는 단어 갯수
        for word in wordsLst:
            for w in word:
                if not learn[ord(w)-ord('a')]:  # 배우지 않은 알파벳이라면
                    break
            else:
                readCnt += 1
        # print(readCnt)
        answer = max(answer, readCnt)   # 최댓값 갱신
        return
    
    for i in range(pos, len(learnLst)):
        num = ord(learnLst[i]) - ord('a')
        if learn[num]:
            continue
        learn[num] = 1        # 알파벳 배우기
        dfs(depth+1, i+1)
        learn[num] = 0        # 복원
        
# main
N, K = map(int, input().split())
if K < 5:
    print(0)
elif K == 5:
    answer = 0
    for _ in range(N):
        word = input().rstrip()
        if len(word) == 8:
            answer += 1
    print(answer)
elif K == 26:
    print(N)
else:
    wordsLst = [set(input().rstrip()) - {'a', 'c', 'i', 'n', 't'} for _ in range(N)]
    learnLst = set()
    for word in wordsLst:
        for char in word:
            learnLst.add(char)
    learn = [0] * 26
    for s in 'acint':
        learn[ord(s)-ord('a')] = 1      # 배움 표시
    answer = 0
    learnLst = list(learnLst)           # 중복 제거한 새로 배울 수 있는 단어 리스트
    print(wordsLst, learnLst)
    dfs(0, 0)
    print(answer)