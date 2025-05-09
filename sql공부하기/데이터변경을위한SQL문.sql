USE market_db;

-- 테이블 생성
CREATE TABLE hongong1 (toy_id INT, toy_name CHAR(4), age INT);
-- 값 넣어주기
INSERT INTO hongong1 VALUES (1,'우디',25);
-- toy_id와 toy_name 만 넣어주기
INSERT INTO hongong1(toy_id, toy_name) VALUES (2,'버즈');
-- 열을 지정해주면 순서 상관없음
INSERT INTO hongong1(toy_name, age, toy_id) VALUES ('제시',20,3);

-- 자동 증가
CREATE TABLE hongong2 (
	toy_id INT AUTO_INCREMENT PRIMARY KEY,
    toy_name CHAR(4),
    age INT);
    
INSERT INTO hongong2 VALUES (NULL, '보핍', 25);
INSERT INTO hongong2 VALUES (NULL, '슬링키', 22);
INSERT INTO hongong2 VALUES (NULL, '렉스', 21);

SELECT * FROM hongong2;

-- 100부터 자동증가 시작하기
ALTER TABLE hongong2 AUTO_INCREMENT=100;
INSERT INTO hongong2 VALUES (NULL, '재남',35);

SELECT * FROM hongong2;

CREATE TABLE hongong3(
	toy_id INT AUTO_INCREMENT PRIMARY KEY,
    toy_name CHAR(4),
    age INT);
ALTER TABLE hongong3 AUTO_INCREMENT=1000;
SET @@auto_increment_increment=3;


-- 다른 테이블의 데이터를 한 번에 입력
SELECT COUNT(*) FROM world.city;

DESC world.city;

SELECT * FROM world.city LIMIT 5;

CREATE TABLE city_popul (city_name CHAR(35), population INT);

INSERT INTO city_popul 
	SELECT Name, Population FROM world.city;
    
SELECT * FROM city_popul;

-- UPDATE 사용
USE market_db;
UPDATE city_popul
	SET city_name='서울'	
	WHERE city_name='Seoul';
SELECT * FROM city_popul WHERE city_name='서울';

UPDATE city_popul
	SET city_name='뉴욕', population=0
    WHERE city_name='New York';
SELECT * FROM city_popul WHERE city_name='뉴욕';


DELETE FROM city_popul
	WHERE city_name LIKE 'New%';
