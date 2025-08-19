CREATE TABLE score(
number INT PRIMARY KEY,
name VARCHAR(60) NOT NULL,
math INT NOT NULL,
english INT NOT NULL);

INSERT INTO score(number, name, math, english) VALUES
(1001, '서민준', 95, 90),
(1002, '이지우', 85, 95),
(1003, '김은서', 90, 85);

SELECT * FROM score;