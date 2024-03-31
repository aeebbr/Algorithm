-- 코드를 작성해주세요
SELECT
    # *
    A.YEAR,
    B.MAX - A.SIZE_OF_COLONY 
        AS YEAR_DEV,
    A.ID
FROM 
    (SELECT *, 
         YEAR(DIFFERENTIATION_DATE) AS YEAR
         FROM ECOLI_DATA
        ) AS A
     JOIN 
        (SELECT 
         YEAR(DIFFERENTIATION_DATE) AS YEAR,
         MAX(SIZE_OF_COLONY) AS MAX
         FROM ECOLI_DATA
         GROUP BY 
            YEAR(DIFFERENTIATION_DATE)
        ) AS B
    ON B.YEAR = A.YEAR
ORDER BY 
    YEAR ASC, 
    YEAR_DEV ASC