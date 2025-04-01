-- 코드를 입력하세요
SELECT user_id, product_id
FROM online_sale
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(sales_amount) >= 2
ORDER BY USER_ID, PRODUCT_ID DESC;