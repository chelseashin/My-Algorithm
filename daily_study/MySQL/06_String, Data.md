### Programmers 코딩테스트 SQL 고득점 KIT



### String, Data



* 루시와 엘라 찾기

  ```sql
  SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
  FROM ANIMAL_INS
  WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
  ORDER BY ANIMAL_ID ASC;
  ```


* 이름에 el이 들어가는 동물 찾기
* ```mysql
  SELECT ANIMAL_ID, NAME
  FROM ANIMAL_INS
  WHERE ANIMAL_TYPE = "Dog" and NAME LIKE "%el%"
  ORDER BY NAME ASC;
  ```



* 중성화 여부 파악하기

  ```sql
  SELECT ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE LIKE "Intact%","X","O") as 중성화
  FROM ANIMAL_INS
  ORDER BY ANIMAL_ID ASC;
  ```


* 오랜 기간 보호한 동물(2)
* ```sql
  SELECT I.ANIMAL_ID, I.NAME
  FROM ANIMAL_INS I
  LEFT OUTER JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
  ORDER BY O.DATETIME - I.DATETIME DESC
  -- ORDER BY DATEDIFF(I.DATETIME, O.DATETIME)
  LIMIT 2;
  ```

* 

* DATETIME에서 DATE로 형 변환
* ```sql
  SELECT ANIMAL_ID, NAME, SUBSTR(DATETIME, 1, 10) as 날짜
  -- SELECT ANIMAL_ID, NAME, LEFT(DATETIME, 10) as 날짜
  -- SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, "%Y-%m-%d") as 날짜
  FROM ANIMAL_INS
  ORDER BY ANIMAL_ID ASC;
  ```

* 