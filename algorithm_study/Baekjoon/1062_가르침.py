import sys
sys.stdin = open('1062_input.txt')

# 하.. 이건 포기,,,

from itertools import combinations
# N, K = map(int, sys.stdin.readline().split())
N, K = map(int, input().split())
basic_set = {'a', 'c', 'i', 'n', 't'}
all_set = set()
word_lst = []
ans = 0

for _ in range(N):
    word_set = set(sys.stdin.readline())
    word_set = word_set - {'\n'}
    diff_set = word_set - basic_set
    word_lst.append(list(diff_set))
    # 합집합
    all_set = all_set.union(word_set)

diff_set = all_set - basic_set
diff_lst = list(diff_set)
diff_lst = sorted(diff_lst)
per = combinations(diff_lst, K - 5)

for spellin in per:
    cnt = 0
    spell_lst = list(spellin) # 알려줄 알파벳 리스트
    for word_gp in word_lst:  # [[r], [c,a,r]] 리스트에서
        is_True = 1
        for word in word_gp : # [c,a,r] -> c, 실제 단어
            if word in spell_lst:
                is_True *= 1
            else:
                is_True *= 0
        if is_True == 1:
            cnt += 1
    ans = max(ans, cnt)

print(ans)