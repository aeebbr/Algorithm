-- 코드를 입력하세요
SELECT 
    MEMBER_ID, 
    MEMBER_NAME, 
    GENDER, 
    -- 생년월일 출력 형식 지정
    DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH 
FROM 
    MEMBER_PROFILE
WHERE
    -- 3월 and 여성만 포함
    -- 전화번호가 null이 아닌 것들만 포함 
    DATE_OF_BIRTH LIKE '%03%'
    AND GENDER = 'W'
    AND TLNO IS NOT NULL
-- 정렬
ORDER BY MEMBER_ID ASC