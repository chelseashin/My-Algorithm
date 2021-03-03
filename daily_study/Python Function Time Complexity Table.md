### Python 내장 함수 시간 복잡도 정리



|      | Operation     | Example       | Class       | Notes                                   |
| ---- | ------------- | ------------- | ----------- | --------------------------------------- |
| 1    | Index         | l[i]          | O(1)        | 인덱스로 값 찾기                        |
| 2    | Store         | l[i] = 0      | O(1)        | 인덱스로 데이터 저장                    |
| 3    | Length        | len(l)        | O(1)        | 리스트 길이                             |
| 4    | Append        | l.append(5)   | O(1)        | 리스드 뒤에 데이터 저장                 |
| 5    | Pop           | l.pop()       | O(1)        | 가장 뒤의 데이터 pop                    |
| 6    | Clear         | l.clear()     | O(1)        | l = []                                  |
| 7    | Slice         | l[a:b]        | O(b-a)      | 슬라이싱되는 요소들 수 만큼 비례        |
| 8    | Extend        | l.extend(...) | O(len(...)) | 확장되는 길이만큼                       |
| 9    | Construction  | list(...)     | O(len(...)) | 리스트 길이만큼                         |
| 10   | check ==, !=  | l1 == l2      | O(N)        | 전체 리스트가 동일한지 확인             |
| 11   | Insert        | l[a:b] = ...  | O(N)        | 데이터 삽입                             |
| 12   | Delete        | del l[i]      | O(N)        | 데이터 삭제                             |
| 13   | Containment   | x in/not in l | O(N)        | 포함 여부 확인                          |
| 14   | Copy          | l.copy()      | O(N)        | 복제                                    |
| 15   | Remove        | l.remove(...) | O(N)        | 제거                                    |
| 16   | Pop           | l.pop(i)      | O(N)        | 제거된 값 이후를 전부 한칸씩 당겨줘야함 |
| 17   | Extreme value | min(l)/max(l) | O(N)        | 전체 데이터를 확인해야함                |
| 18   | Reverse       | l.reverse()   | O(N)        | 뒤집기                                  |
| 19   | Iteration     | for v in l:   | O(N)        | 전체 데이터 확인하므로                  |
| 20   | Sort          | l.sort()      | O(N Log N)  | 파이썬 기본 정렬 알고리즘               |
| 21   | Multiply      | k*l           | O(k N)      | 리스트의 곱은 리스트 개수 늘어남        |