### Programmers 코딩테스트 SQL 고득점 KIT



### JOIN



* 없어진 기록 찾기

  ```mysql
  -- 조인 이용
  SELECT O.ANIMAL_ID, O.NAME
  FROM ANIMAL_OUTS AS O
  LEFT OUTER JOIN ANIMAL_INS AS I
  ON O.ANIMAL_ID = I.ANIMAL_ID
  WHERE I.ANIMAL_ID is NULL;
  ```


* 있었는데요 없었습니다
* ```mysql
  -- INNER JOIN
  SELECT O.ANIMAL_ID, O.NAME
  FROM ANIMAL_OUTS O
  INNER JOIN ANIMAL_INS I ON O.ANIMAL_ID = I.ANIMAL_ID
  WHERE I.DATETIME > O.DATETIME
  ORDER BY I.DATETIME ASC;
  
  -- LEFT JOIN / LEFT OUTER JOIN 모두 가능
  SELECT O.ANIMAL_ID, O.NAME
  FROM ANIMAL_OUTS O
  LEFT JOIN ANIMAL_INS I ON O.ANIMAL_ID = I.ANIMAL_ID
  WHERE O.DATETIME < I.DATETIME
  ORDER BY I.DATETIME ASC;
  
  -- 조인 사용 X
  SELECT I.ANIMAL_ID, I.NAME
  FROM ANIMAL_INS I, ANIMAL_OUTS O
  WHERE I.ANIMAL_ID = O.ANIMAL_ID AND I.DATETIME > O.DATETIME
  ORDER BY I.DATETIME;
  ```



* 오랜 기간 보호한 동물(1)
* ```mysql
  -- LEFT JOIN / LEFT OUTER JOIN 모두 가능
  SELECT I.NAME, I.DATETIME
  FROM ANIMAL_INS as I
  LEFT JOIN ANIMAL_OUTS as O
  -- LEFT OUTER JOIN ANIMAL_OUTS as O
  ON I.ANIMAL_ID = O.ANIMAL_ID
  WHERE O.ANIMAL_ID IS NULL
  ORDER BY I.DATETIME ASC LIMIT 3;
  ```



* 보호소에서 중성화한 동물

  ```mysql
  -- LEFT JOIN, LEFT OUTER JOIN, INNER JOIN 모두 가능
  SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
  FROM ANIMAL_INS I
  INNER JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
  WHERE I.SEX_UPON_INTAKE LIKE "Intact%" AND O.SEX_UPON_OUTCOME NOT LIKE "Intact%"
  # (O.SEX_UPON_OUTCOME LIKE "Spayed%" OR O.SEX_UPON_OUTCOME LIKE "Neutered%")
  ORDER BY O.ANIMAL_ID ASC;
  ```
