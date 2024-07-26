CREATE DATABASE AirportManagement;


USE AirportManagement;


CREATE TABLE AIRPORT(
    NO_OF_TERMINALS INT,
    AID INT PRIMARY KEY,
    AIRPORT_NAME VARCHAR(20) NOT NULL,
    CITY VARCHAR(15),
    AREA VARCHAR(15),
    ACOUNTRY VARCHAR(15),
    TIMEZONE VARCHAR(10)
);


CREATE TABLE PAYMENT(
    PAYID INT PRIMARY KEY,
    PAYDATE VARCHAR(10),
    PAYABLE_AMOUNT DECIMAL(10,2) NOT NULL,
    PAY_METHOD VARCHAR(20),
    PAYMENT_STATUS VARCHAR(20)
);


CREATE TABLE PASSENGER(
    PID INT PRIMARY KEY,
    NAME VARCHAR(20) NOT NULL,
    PHONE VARCHAR(10) NOT NULL UNIQUE,
    EMAIL VARCHAR(20),
    DOB DATE,
    AGE INT,
    PASSPORTNO VARCHAR(10) NOT NULL UNIQUE,
    ADDRESS VARCHAR(20),
    NATIONALITY VARCHAR(10)
);


CREATE TABLE AIRLINE(
    AIRLINEID INT PRIMARY KEY,
    AIRLINENAME VARCHAR(15) NOT NULL UNIQUE,
    HELPLINENO INT NOT NULL,
    COUNTRY VARCHAR(20),
    ACODE VARCHAR(5) NOT NULL
);


CREATE TABLE BOOKING(
    BID INT PRIMARY KEY,
    BDATE DATE,
    BSTATUS VARCHAR(9),
    AMOUNT DECIMAL(10,2) NOT NULL,
    PAYMENTSTATUS VARCHAR(8),
    PID INT,
    FOREIGN KEY(PID) REFERENCES PASSENGER(PID),
    PAYID INT,
    FOREIGN KEY(PAYID) REFERENCES PAYMENT(PAYID),
    NO_OF_SEATS INT NOT NULL
);


CREATE TABLE FLIGHT(
    FID INT PRIMARY KEY,
    FNO INT NOT NULL,
    DEPARTURE VARCHAR(15) NOT NULL,
    ARRIVAL DATETIME NOT NULL,
    STATUS VARCHAR(10),
    AIRLINEID INT,
    FOREIGN KEY(AIRLINEID) REFERENCES AIRLINE(AIRLINEID)
);


CREATE TABLE TICKET(
    TICKET_ID INT PRIMARY KEY,
    SEAT_NO VARCHAR(10) NOT NULL,
    CLASS VARCHAR(10),
    BID INT,
    FOREIGN KEY(BID) REFERENCES BOOKING(BID),
    FID INT,
    FOREIGN KEY(FID) REFERENCES FLIGHT(FID),
    AID INT,
    FOREIGN KEY(AID) REFERENCES AIRPORT(AID),
    AIRLINEID INT,
    FOREIGN KEY(AIRLINEID) REFERENCES AIRLINE(AIRLINEID),
    PID INT,
    FOREIGN KEY(PID) REFERENCES PASSENGER(PID),
    DEPARTING_FROM VARCHAR(20) NOT NULL,
    ARRIVING_AT VARCHAR(20) NOT NULL
);
CREATE TABLE USERS(
    username VARCHAR(15) PRIMARY KEY,
    PWD VARCHAR(15) NOT NULL
);
