### Programmers 코딩테스트 SQL 고득점 KIT



#### SUM, MAX, MIN

* 최댓값 구하기

  ```mysql
  # MAX 사용한 권장 풀이
  SELECT MAX(DATETIME) AS 시간
  FROM ANIMAL_INS;
  
  # 정렬 후 top 1만 뽑은 풀이
  SELECT DATETIME AS 시간
  FROM ANIMAL_INS
  ORDER BY DATETIME
  LIMIT 1;
  ```


* 최솟값 구하기

  ```mysql
  # MIN 사용한 권장 풀이
  SELECT MIN(DATETIME) as 시간
  FROM ANIMAL_INS;
  
  # 정렬 후 top 1만 뽑은 풀이
  SELECT DATETIME as 시간
  FROM ANIMAL_INS
  ORDER BY DATETIME ASC LIMIT 1;
  ```



* 동물 수 구하기

  ```mysql
  SELECT COUNT(*) as count
  FROM ANIMAL_INS;
  ```


* 중복 제거하기

  ```mysql
  SELECT COUNT(DISTINCT(NAME)) as count
  FROM ANIMAL_INS
  WHERE NAME IS NOT NULL;
  ```
