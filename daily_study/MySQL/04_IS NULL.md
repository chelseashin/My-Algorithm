### Programmers 코딩테스트 SQL 고득점 KIT



### IS NULL



* 이름이 없는 동물의 아이디

  ```mysql
  SELECT ANIMAL_ID
  FROM ANIMAL_INS
  WHERE NAME IS NULL;
  ```



* 이름이 있는 동물의 아이디

  ```mysql
  SELECT ANIMAL_ID
  FROM ANIMAL_INS
  WHERE NAME IS NOT NULL
  ORDER BY ANIMAL_ID ASC;
  ```


* NULL 처리하기

    ```sql
  SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') AS NAME, SEX_UPON_INTAKE
  FROM ANIMAL_INS
  WHERE NAME IS NOT NULL
  ORDER BY ANIMAL_ID ASC;
    ```
