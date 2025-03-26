## ✈️ Airlines Management System

### 🌍 Overview

The Airlines Management System is a software solution designed to demonstrate CRUD (Create, Read, Update, Delete) operations for managing an airline's daily operations. This system allows users to efficiently manage flights, passengers, and bookings.

The project features a user-friendly Streamlit frontend, a Python-powered backend, and an SQL database for structured data management.

### 🛠️ Features

- 🛫 **Flight Management**: Admins can add, update, delete, and view flights.
- 🤝 **Passenger Management**: Admins can view, add, and update passenger details.
- 🌐 **Booking System**: Passengers can book flights, view history, and cancel bookings.
- 💎 **Ticket Management**: Admins can manage and assign tickets.
- 🔍 **Search Functionality**: Users can search for flights by destination, date, and available seats.

### 👨‍💻 Technologies Used

- **Python** 💻 - Backend logic and CRUD operations.
- **Streamlit** 🌟 - Interactive frontend UI.
- **SQL** 📂 - Database management.
- **SQLite** 📃 - Lightweight database for storing records.

### 📁 Database Overview

The system uses multiple tables to organize airline operations efficiently:

- 🛏️ **AIRPORT**: Stores airport details (name, location, terminals).
- 💳 **PAYMENT**: Manages booking payments (status, method).
- 👤 **PASSENGER**: Stores passenger details (personal info, passport number).
- 🌏 **AIRLINE**: Contains airline information (name, country).
- 🌄 **BOOKING**: Manages bookings (status, amount, passenger, payment).
- ✈️ **FLIGHT**: Stores flight details (flight number, departure, arrival).
- 🏷️ **TICKET**: Links passengers to booked tickets (seat number, flight, class).
- 🛡️ **USERS**: Stores admin login credentials.

### 🛠️ Installation & Setup

#### 📚 Step 1: Clone the repository
```sh
git clone https://github.com/yourusername/airlines-management-system.git
```

#### 🏢 Step 2: Navigate to the project directory
```sh
cd DBMS_PROJECT
```

#### ⚙️ Step 3: Install dependencies manually

```sh
pip install streamlit sqlite3 pandas
```

#### 📝 Step 4: Set up the database in your localhost

#### 🎮 Step 5: Run the application
```sh
streamlit run code6_final_real.py
```

### 🎨 Contributing

Want to make this project even better? Fork the repository, make your magic happen, and submit a pull request!

🚀 Your contributions are like first-class upgrades for this pr