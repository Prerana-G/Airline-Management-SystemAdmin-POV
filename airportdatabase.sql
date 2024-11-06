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
CREATE TABLE users (
	username VARCHAR(50) NOT NULL Primary Key,
	pwd VARCHAR(255) NOT NULL,
	role VARCHAR(50) NOT NULL );


select * from passenger;
select * from airport;
select * from airline;
select * from payment;
select * from flight;
select * from booking;
select * from ticket;
select * from users;

INSERT INTO AIRPORT (NO_OF_TERMINALS, AID, AIRPORT_NAME, CITY, AREA, ACOUNTRY, TIMEZONE) VALUES
(4, 1, 'Kempegowda Intl', 'Bangalore', 'Devanahalli', 'India', 'IST'),
(3, 2, 'Mangalore Intl', 'Mangalore', 'Bajpe', 'India', 'IST'),
(2, 3, 'Hubli Airport', 'Hubli', 'Gokul Rd', 'India', 'IST'),
(4, 4, 'Chhatrapati Shivaji', 'Mumbai', 'Andheri', 'India', 'IST'),
(3, 5, 'Indira Gandhi', 'Delhi', 'Palam', 'India', 'IST'),
(2, 6, 'Netaji Subhas', 'Kolkata', 'Dum Dum', 'India', 'IST'),
(3, 7, 'Chennai Intl', 'Chennai', 'Meenambakkam', 'India', 'IST'),
(2, 8, 'Goa Intl', 'Goa', 'Dabolim', 'India', 'IST');

INSERT INTO PAYMENT (PAYID, PAYDATE, PAYABLE_AMOUNT, PAY_METHOD, PAYMENT_STATUS) VALUES
(1, '2024-07-20', 1500.50, 'Credit Card', 'Completed'),
(2, '2024-07-21', 2300.75, 'Debit Card', 'Pending'),
(3, '2024-07-22', 1200.00, 'Net Banking', 'Completed'),
(4, '2024-07-23', 800.20, 'UPI', 'Failed'),
(5, '2024-07-24', 5400.90, 'Credit Card', 'Completed'),
(6, '2024-07-25', 3200.30, 'Debit Card', 'Pending'),
(7, '2024-07-26', 2150.45, 'Net Banking', 'Completed'),
(8, '2024-07-27', 765.60, 'UPI', 'Completed');


INSERT INTO PASSENGER (PID, NAME, PHONE, EMAIL, DOB, AGE, PASSPORTNO, ADDRESS, NATIONALITY) VALUES
(1, 'Rajesh Kumar', '9876543210', 'rajesh.kumr@gml.com', '1990-01-15', 34, 'A12345678', 'Bangalore', 'Indian'),
(2, 'Priya Sharma', '9876543211', 'priya.sharm@yhoo.com', '1985-03-25', 39, 'A23456789', 'Mumbai', 'Indian'),
(3, 'Anil Patel', '9876543212', 'anil.patel@otlk.com', '1978-07-14', 45, 'A34567890', 'Ahmedabad', 'Indian'),
(4, 'Neha Rao', '9876543213', 'neha.rao@gml.com', '1995-11-30', 28, 'A45678901', 'Hyderabad', 'Indian'),
(5, 'Sunil Menon', '9876543214', 'sunil.meno@yhoo.com', '1988-04-10', 36, 'A56789012', 'Kochi', 'Indian'),
(6, 'Meena Iyer', '9876543215', 'meena.iyer@otlk.com', '1993-12-01', 30, 'A67890123', 'Chennai', 'Indian'),
(7, 'Vikram Singh', '9876543216', 'vikram.sing@gml.com', '1982-08-21', 41, 'A78901234', 'Delhi', 'Indian'),
(8, 'Aarti Desai', '9876543217', 'aarti.desy@yhoo.com', '1999-02-05', 25, 'A89012345', 'Pune', 'Indian');

INSERT INTO AIRLINE (AIRLINEID, AIRLINENAME, HELPLINENO, COUNTRY, ACODE) VALUES
(1, 'Air India', 1234567890, 'India', 'AI'),
(2, 'IndiGo', 1234567891, 'India', '6E'),
(3, 'SpiceJet', 1234567892, 'India', 'SG'),
(4, 'Vistara', 1234567893, 'India', 'UK'),
(5, 'GoAir', 1234567894, 'India', 'G8'),
(6, 'AirAsia', 1234567895, 'India', 'I5'),
(7, 'Jet Airways', 1234567896, 'India', '9W'),
(8, 'Alliance Air', 1234567897, 'India', '9I');

INSERT INTO BOOKING (BID, BDATE, BSTATUS, AMOUNT, PAYMENTSTATUS, PID, PAYID, NO_OF_SEATS) VALUES
(1, '2024-07-20', 'Confirmed', 1500.50, 'Completed', 1, 1, 1),
(2, '2024-07-21', 'Pending', 2300.75, 'Pending', 2, 2, 2),
(3, '2024-07-22', 'Confirmed', 1200.00, 'Completed', 3, 3, 1),
(4, '2024-07-23', 'Cancelled', 800.20, 'Failed', 4, 4, 1),
(5, '2024-07-24', 'Confirmed', 5400.90, 'Completed', 5, 5, 3),
(6, '2024-07-25', 'Pending', 3200.30, 'Pending', 6, 6, 2),
(7, '2024-07-26', 'Confirmed', 2150.45, 'Completed', 7, 7, 1),
(8, '2024-07-27', 'Confirmed', 765.60, 'Completed', 8, 8, 1);




INSERT INTO FLIGHT (FID, FNO, DEPARTURE, ARRIVAL, STATUS, AIRLINEID) VALUES
(1, 101, 'Bangalore', '2024-07-20 08:00:00', 'On Time', 1),
(2, 102, 'Mumbai', '2024-07-21 09:30:00', 'Delayed', 2),
(3, 103, 'Delhi', '2024-07-22 10:45:00', 'On Time', 3),
(4, 104, 'Kolkata', '2024-07-23 12:00:00', 'Cancelled', 4),
(5, 105, 'Chennai', '2024-07-24 14:15:00', 'On Time', 5),
(6, 106, 'Goa', '2024-07-25 16:30:00', 'Delayed', 6),
(7, 107, 'Hyderabad', '2024-07-26 18:00:00', 'On Time', 7),
(8, 108, 'Pune', '2024-07-27 20:00:00', 'On Time', 8);

INSERT INTO TICKET (TICKET_ID, SEAT_NO, CLASS, BID, FID, AID, AIRLINEID, PID, DEPARTING_FROM, ARRIVING_AT) VALUES
(1, 'A1', 'Economy', 1, 1, 1, 1, 1, 'Bangalore', 'Delhi'),
(2, 'B1', 'Business', 2, 2, 4, 2, 2, 'Mumbai', 'Bangalore'),
(3, 'C1', 'Economy', 3, 3, 5, 3, 3, 'Delhi', 'Mumbai'),
(4, 'D1', 'First', 4, 4, 6, 4, 4, 'Kolkata', 'Chennai'),
(5, 'E1', 'Economy', 5, 5, 7, 5, 5, 'Chennai', 'Kolkata'),
(6, 'F1', 'Business', 6, 6, 8, 6, 6, 'Goa', 'Hyderabad'),
(7, 'G1', 'Economy', 7, 7, 2, 7, 7, 'Hyderabad', 'Goa'),
(8, 'H1', 'First', 8, 8, 3, 8, 8, 'Pune', 'Delhi');

alter table airline modify helplineno varchar(20);









