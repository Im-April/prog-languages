USE market_db;

-- ORDER BY
SELECT mem_id, mem_name, debut_date
	FROM member
    ORDER BY debut_date ASC; -- 오름차순
    
SELECT mem_id, mem_name, debut_date
	FROM member
    ORDER BY debut_date DESC; -- 내림차순
    
SELECT mem_id, mem_name, debut_date, height
	FROM member
    WHERE height >= 164
    ORDER BY height DESC;
    
SELECT mem_id, mem_name, debut_date, height
	FROM member
    WHERE height >= 164
    ORDER BY height DESC, debut_date ASC;
    
-- LIMIT : 출력 개수 제한
SELECT *
	FROM member
    LIMIT 3;
    
SELECT mem_name, debut_date
	FROM member
    ORDER BY debut_date ASC;
    
SELECT mem_name, debut_date
	FROM member
    ORDER BY debut_date ASC
    LIMIT 3, 2;
    
-- DISTINCT
SELECT addr FROM member;

SELECT DISTINCT addr FROM member;

-- GROUP BY
SELECT mem_id, SUM(amount) 
	FROM buy 
    GROUP BY mem_id;
    
SELECT mem_id, SUM(price*amount)
	FROM buy
    GROUP BY mem_id; -- 구매한 금액의 총합

SELECT AVG(amount)
	FROM buy; -- 전체 회원의 평균 구매 횟수
    
SELECT mem_id, AVG(amount)
	FROM buy
    GROUP BY mem_id;
    
    
-- COUNT
SELECT COUNT(phone1) FROM member; -- 전화번호가 있는 회원 수

-- HAVING절
SELECT mem_id, SUM(price*amount)
	FROM buy
    GROUP BY mem_id
    HAVING SUM(price*amount) > 1000
    ORDER BY SUM(price*amount) DESC;