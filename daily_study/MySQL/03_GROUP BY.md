### Programmers 코딩테스트 SQL 고득점 KIT



#### GROUP BY



* 고양이와 개는 몇 마리 있을까
* ```mysql
  SELECT ANIMAL_TYPE, COUNT(*) as count
  FROM ANIMAL_INS
  GROUP BY ANIMAL_TYPE
  ORDER BY ANIMAL_TYPE;
  ```

* 

* 동명 동물 수 찾기

  ```mysql
  SELECT NAME, COUNT(*) AS COUNT
  FROM ANIMAL_INS
  WHERE NAME IS NOT NULL
  GROUP BY NAME
  HAVING COUNT(NAME) >= 2
  ORDER BY NAME;
  ```


* 입양 시각 구하기(1)

  ```mysql
  SELECT HOUR(DATETIME) as HOUR, count(*) as COUNT
  FROM ANIMAL_OUTS
  GROUP BY HOUR
  HAVING HOUR BETWEEN 9 and 19
  ORDER BY HOUR;
  ```



* 입양 시각 구하기(2)

  ```mysql
  SET @HOUR = -1;
  SELECT @HOUR := @HOUR + 1 AS HOUR, (select count(*) from animal_outs where hour(datetime) = @hour) AS COUNT
  FROM ANIMAL_OUTS
  GROUP BY HOUR
  HAVING HOUR BETWEEN 0 AND 23
  ORDER BY HOUR;
  ```
