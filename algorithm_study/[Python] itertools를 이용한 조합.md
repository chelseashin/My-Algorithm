## [Python] itertools를 이용한 조합



2020-07-10



Python 내장 라이브러리인 itertools는 Python에서 제공하는 자신만의 반복자를 만드는 휼륭한 모듈입니다. 특정 배열에 대하여 순열이나 조합을 만들어 이를 이용하는 문제를 풀 때, 직접 구현해도 되지만, 이 itertools를 이용한다면 효율적으로 반복자를 구할 수 있습니다.

```
# 1. product : 복원 순열
# 2. permutation : (비복원) 순열
# 3. combinations_with_replacement : 복원 조합
# 4. combinations : (비복원) 조합
```

ex) from itertools import permutations 선언

### product()

```python
.import itertools
 
itertools.product('ABCD', repeat=2)
# 결과: AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
```

**인수**: p, q, ... [ 반복 = 1 ]

**결과**: 중첩된 for loop에 해당하는 데카르트의 곱



----

### permutations()

```python
import itertools
 
itertools.permutations('ABCD', 2)
# 결과: AB AC AD BA BC BD CA CB CD DA DB DC
```

**인수**: `p \[, r\]`

**결과**: `r` 길이 tuple, 가능한 모든 순서, 반복 X



----

### combinations()

```python
import itertools
 
itertools.combinations('ABCD', 2)
# 결과: AB AC AD BC BD CD
```

**인수**: `p`, `r`

**결과**: r 길이 tuple, 정렬된 순서, 반복 X



----

### combinations_with_replacement()

```python
import itertools
 
itertools.combinations_with_replacement('ABCD', 2)
# 결과: AA AB AC AD BB BC BD CC CD DD
```

**인수**: `p`, `r`

**결과**: `r` 길이 tuple, 정렬된 순서, 반복 O

| **반복자**                      | **인수**               | **결과**                                 |
| ------------------------------- | ---------------------- | ---------------------------------------- |
| product()                       | p, q, ... [ 반복 = 1 ] | 중첩된 for loop에 해당하는 데카르트의 곱 |
| permutations()                  | p [, r]                | r 길이 tuple, 가능한 모든 순서, 반복 X   |
| combinations()                  | p, r                   | r 길이 tuple, 정렬된 순서, 반복 X        |
| combinations_with_replacement() | p, r                   | r 길이 tuple, 정렬된 순서, 반복 O        |

