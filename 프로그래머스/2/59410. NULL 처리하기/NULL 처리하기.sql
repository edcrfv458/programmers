-- 코드를 입력하세요
SELECT ANIMAL_TYPE, 
       case when NAME IS NULL then "No name"
       else NAME  end "NAME", 
       SEX_UPON_INTAKE
FROM ANIMAL_INS