-- 현재 사용하는 데이터베이스 지정
USE market_db;

-- SELECT문 기본 형식
SELECT * FROM member;

-- 특정 열만 출력
SELECT mem_name FROM member;

-- 열 이름 별칭
SELECT addr 주소, debut_date "데뷔 일자" , mem_name FROM member;

-- 기본적 WHERE 절
SELECT mem_id, mem_name
	FROM member
    WHERE height >= 165;
    
-- WHERE절 AND
SELECT mem_id, mem_name
	FROM member
    WHERE height >= 165 AND mem_number > 6;
    
-- WHERE절 OR
SELECT mem_id, mem_name
	FROM member
    WHERE height >= 165 OR mem_number > 6;
    
-- BETWEEN ~ AND 사용
SELECT mem_name, height
	FROM member
    WHERE height >= 163 AND height <= 165; -- 163이상 165이하
    
SELECT mem_name, height
	FROM member
	WHERE height BETWEEN 163 AND 165;
    
-- IN() 사용
SELECT mem_name, addr
	FROM member
    WHERE addr='경기' OR addr='전남' OR  addr='경남';
    
SELECT mem_name, addr
	FROM member
    WHERE addr IN ('경기','전남','경남');


-- LIKE 
SELECT *
	FROM member
    WHERE mem_name LIKE '우%';
    
SELECT *
	FROM member
    WHERE mem_name LIKE '__핑크';