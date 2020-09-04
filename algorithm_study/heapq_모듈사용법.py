# 데이터를 정렬된 상태로 저장하기 위해 사용하는
# 파이썬의 heapq(힙큐) 내장 모듈

# 자세한 설명은 typora 참고

# heapq 임포트
# from heapq import heappush, heappop
import heapq

# 최초 힙 생성
heap = []

# 힙에  원소 추가
# 첫 번째 인자는 원소를 추가할 대상 리스트,
# 두 번째 인자는 추가할 원소를 넘김
heapq.heappush(heap, 6)
heapq.heappush(heap, 5)
heapq.heappush(heap, 7)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print(heap)

# 힙에서 원소 삭제
print(heapq.heappop(heap))
print(heap)

print(heapq.heappop(heap))
print(heap)

# 최소값 삭제하지 않고 얻기
print(heap[0])

# 기존 리스트를 힙으로 변환
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap)