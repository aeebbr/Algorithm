-- 코드를 입력하세요
SELECT
    # *,
    C.CAR_ID,
    C.CAR_TYPE,
    ROUND(C.DAILY_FEE * ((100 - P.DISCOUNT_RATE) * 0.01)) * 30 AS FEE
FROM 
    CAR_RENTAL_COMPANY_CAR AS C
    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
    ON C.CAR_ID = H.CAR_ID
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS P
    ON C.CAR_TYPE = P.CAR_TYPE
WHERE 
    C.CAR_TYPE IN ('세단', 'SUV')
    AND P.DURATION_TYPE LIKE '30%'
    # (정가 * (((100-할인율) * 0.01)))
    AND (
        (C.DAILY_FEE * ((100 - P.DISCOUNT_RATE) * 0.01)) * 30 >= 500000
        AND (C.DAILY_FEE * ((100 - P.DISCOUNT_RATE) * 0.01)) * 30 < 2000000
    ) 
    AND (
        # 대여 불가한 날이 있는 차를 제외 
        H.CAR_ID NOT IN (
            SELECT CAR_ID
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
            WHERE 
                # 30일 이전에 시작, 1일 이전에 종료되는 차들은 대여 불가 
                START_DATE <= '2022-11-30' AND END_DATE >= '2022-11-01'
        )
    )
GROUP BY 
    C.CAR_ID
ORDER BY 
    FEE DESC,
    C.CAR_TYPE ASC, 
    C.CAR_ID DESC