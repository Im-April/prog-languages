INSERT INTO member(name, phone, address) VALUES
('박소은','010-1111-1111','서울시 마포구'),
('송광호','010-2222-2222','경기도 김포시'),
('노승진','010-3333-3333','제주도 제주시');

SELECT * FROM member;

INSERT INTO reservations(user_number, reservation_number) VALUES
(1, '박소은'),
(2, '송광호'),
(3, '노승진');

# 컬럼명과 데이터형 바꾸기
ALTER TABLE reservations 
CHANGE reservation_number name VARCHAR(60);

ALTER TABLE reservations 
CHANGE user_number reservation_number VARCHAR(60);

SELECT * FROM reservations;
