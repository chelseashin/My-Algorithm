# Brute Force
# 브루트 포스(Brute Force)는 거의 모든 문제에 사용할 수 있는 기법으로 완전 탐색이라고도 합니다.
#  이 기법은 이름처럼,
# "맹목적으로, 모든 경우의 수를 탐색하여 결과를 도출하는 기법"입니다.
# 이 기법은 어쩔수없이 모든 경우의 수를 탐색해 봐야만 하는 경우나,
# 모든 경우의 수를 요구하는 문제에서 주로 사용됩니다.

# 재귀로 순열 구하기

iterable = [1, 2, 3, 4, 5]
visited = [0] * 5

def get_permutations(_currentIndex, _permutation):
    if _currentIndex == 5:
        print(_permutation)
        return

    for index, value in enumerate(iterable):
        if not visited[index]:
            visited[index] = 1
            _permutation[_currentIndex] = value
            get_permutations(_currentIndex + 1, _permutation)
            visited[index] = 0

if __name__ == '__main__':
    get_permutations(0, [0] * 5)