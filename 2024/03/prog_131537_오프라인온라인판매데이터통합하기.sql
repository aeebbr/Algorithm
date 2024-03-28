-- 코드를 입력하세요
SELECT
    # * 
    DATE_FORMAT(A.SALES_DATE, '%Y-%m-%d') AS SALES_DATE, 
    PRODUCT_ID, 
    A.USER_ID, 
    SALES_AMOUNT
FROM (
    SELECT 
        SALES_DATE, 
        PRODUCT_ID, 
        USER_ID, 
        SALES_AMOUNT
    FROM 
        ONLINE_SALE
    UNION ALL 
    SELECT 
        SALES_DATE, 
        PRODUCT_ID, 
        NULL AS USER_ID, 
        SALES_AMOUNT
    FROM 
        OFFLINE_SALE 
) AS A
WHERE 
    A.SALES_DATE LIKE '2022-03-%'
ORDER BY 
    A.SALES_DATE ASC, 
    A.PRODUCT_ID ASC, 
    A.USER_ID ASC