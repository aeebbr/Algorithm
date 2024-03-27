-- 코드를 작성해주세요
SELECT 
    I.ITEM_ID,
    I.ITEM_NAME,
    I.RARITY
FROM 
    ITEM_INFO AS I 
    INNER JOIN ITEM_TREE AS T
        ON I.ITEM_ID = T.ITEM_ID
WHERE  
    T.PARENT_ITEM_ID IN (SELECT ITEM_ID
                        FROM ITEM_INFO
                        WHERE RARITY='RARE')
ORDER BY 
    I.ITEM_ID DESC