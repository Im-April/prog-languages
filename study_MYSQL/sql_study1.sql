CREATE TABLE member(
    member_num INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(60) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(100) NOT NULL
);

CREATE TABLE reservations (
    user_number INT NOT NULL PRIMARY KEY,
    reservation_number VARCHAR(20) NOT NULL
);