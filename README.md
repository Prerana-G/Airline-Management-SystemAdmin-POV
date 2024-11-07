# Airline-Management-SystemAdmin-POV
This project is an Airport Ticket Booking Management System for Administrators, designed for three types of admins with role-specific access to various tables. It leverages Streamlit for the user interface and MySQL for backend data management. Admins are assigned roles (Employee, Manager, Board Member), each with specific access rights, allowing for role-based control over the airport and ticket management database. Admins can perform CRUD (Create, Read, Update, Delete) operations on tables like bookings, passengers, payments, and flights as per their role.

# Airport Ticket Booking Management System for Admins

## Overview
This project is a web-based management system tailored for **administrative users** handling airport ticket bookings. Developed using **Streamlit** and **MySQL**, the system supports three types of admin roles, each with specific access to various tables in the database.

### Admin Roles and Access
- **Employee**: Access to `PAYMENT`, `PASSENGER`, `BOOKING`, `FLIGHT`, and `TICKET` tables.
- **Manager**: Access to all tables available to Employees, plus `AIRPORT` and `AIRLINE`.
- **Board Member**: Full access to all tables, including `AIRPORT`, `AIRLINE`, `PASSENGER`, `FLIGHT`, `BOOKING`, `TICKET`, and `PAYMENT`.

## Features
- **Role-Based Access Control**: Admins are assigned roles (Employee, Manager, Board Member) with access rights specific to each role.
- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on tables relevant to each admin role.
- **Secure Authentication**: Password hashing ensures secure login and access control.
- **Data Sorting and Searching**: Quickly sort and search through records within permitted tables.

## Project Structure
- `airlinePage.py`: Contains the main application logic, including database connection setup, CRUD operations, and role-based access control via the Streamlit interface.
- `users.py`: A secondary script for managing hardcoded users and authentication processes.

## Setup and Installation
1. **Install Dependencies**: 
   ```bash
   pip install streamlit mysql-connector-python pandas
2. **Database Configuration**: Ensure a MySQL server is running, then update database credentials in airlinePage.py with the appropriate MySQL configuration.

3. **Run the Application**:
streamlit run airlinePage.py

**Usage**
Admin Login: Each admin logs in with their credentials, and role-based access is granted automatically.
Table Access:
Employees can manage essential tables like PAYMENT, PASSENGER, and BOOKING.
Managers and Board Members have expanded access, with Board Members having full control over all tables.
Logout: Admins can securely log out when finished.
