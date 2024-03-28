-- 코드를 작성해주세요
SELECT 
    COUNT(I.ID) AS FISH_COUNT, 
    N.FISH_NAME    
FROM 
    FISH_INFO AS I
    JOIN FISH_NAME_INFO AS N 
    ON I.FISH_TYPE = N.FISH_TYPE 
GROUP BY 
    N.FISH_NAME
ORDER BY 
    FISH_COUNT DESC 
    