import mysql.connector
import pandas as pd
import streamlit as st
import hashlib

# Database connection
def create_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Pragnya12#',
        database='AirportManagement'
    )

# Hash password
def hash_password(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

# Register user
def register_user(username, pwd):
    hashed_password = hash_password(pwd)
    try:
        conn = create_connection()
        cursor = conn.cursor()
        query = "INSERT INTO users (username, pwd) VALUES (%s, %s)"
        cursor.execute(query, (username, hashed_password))
        conn.commit()
        conn.close()
        return True
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        conn.rollback()
        conn.close()
        return False

# Check if record exists
def record_exists(table, id_column, id_value):
    conn = create_connection()
    cursor = conn.cursor()
    query = f'SELECT 1 FROM {table} WHERE {id_column} = %s'
    cursor.execute(query, (id_value,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

# CRUD operations
def insert_record(table, **kwargs):
    conn = create_connection()
    cursor = conn.cursor()
    columns = ', '.join(kwargs.keys())
    placeholders = ', '.join(['%s'] * len(kwargs))
    query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
    cursor.execute(query, tuple(kwargs.values()))
    conn.commit()
    conn.close()

def read_records(table):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table}')
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    conn.close()
    return rows, columns

def update_record(table, id_column, id_value, **kwargs):
    if not record_exists(table, id_column, id_value):
        return False
    conn = create_connection()
    cursor = conn.cursor()
    updates = ', '.join([f'{k} = %s' for k in kwargs])
    query = f'UPDATE {table} SET {updates} WHERE {id_column} = %s'
    cursor.execute(query, (*kwargs.values(), id_value))
    conn.commit()
    conn.close()
    return True

def delete_record(table, id_column, id_value):
    if not record_exists(table, id_column, id_value):
        return False
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {table} WHERE {id_column} = %s', (id_value,))
    conn.commit()
    conn.close()
    return True

# Streamlit app
def main():
    st.title("Airport Management System")

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
        st.session_state["username"] = None

    menu = ["Register", "Login", "CRUD Operations"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Register":
        st.subheader("Create New Account")
        username = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        confirm_pwd = st.text_input("Confirm Password", type="password")

        if st.button("Register"):
            if pwd == confirm_pwd:
                if register_user(username, pwd):
                    st.success("You have successfully created an account!")
                else:
                    st.error("Username not available. Try again with a different username.")
            else:
                st.error("Passwords do not match.")

    elif choice == "Login":
        st.subheader("Login Section")
        username = st.text_input("Username")
        pwd = st.text_input("Password", type="password")

        if st.button("Login"):
            # Placeholder for login logic
            st.success("Logged in successfully!")
            st.warning("Login functionality not implemented in this example.")
            st.session_state["logged_in"] = True
            st.session_state["username"] = username

    elif choice == "CRUD Operations":
        if st.session_state["logged_in"]:
            st.subheader(f"Welcome, {st.session_state['username']}!")

            # Add background image
            background_image_html = """
            <style>
            .stApp {
                background-image: url('https://www.example.com/path/to/your/image.jpg');
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }
            </style>
            """
            st.markdown(background_image_html, unsafe_allow_html=True)

            st.title("Airport Management")

            menu = ["Create", "Read", "Update", "Delete"]
            choice = st.sidebar.selectbox("Select Operation", menu)

            table = st.selectbox("Select Table", ["AIRPORT", "PAYMENT", "PASSENGER", "AIRLINE", "BOOKING", "FLIGHT", "TICKET"])

            fields = {
                "AIRPORT": ["AID", "AIRPORT_NAME", "CITY", "AREA", "ACOUNTRY", "TIMEZONE", "NO_OF_TERMINALS"],
                "PAYMENT": ["PAYID", "PAYDATE", "PAYABLE_AMOUNT", "PAY_METHOD", "PAYMENT_STATUS"],
                "PASSENGER": ["PID", "NAME", "PHONE", "EMAIL", "DOB", "AGE", "PASSPORTNO", "ADDRESS", "NATIONALITY"],
                "AIRLINE": ["AIRLINEID", "AIRLINENAME", "HELPLINENO", "COUNTRY", "ACODE"],
                "BOOKING": ["BID", "BDATE", "BSTATUS", "AMOUNT", "PAYMENTSTATUS", "PID", "PAYID", "NO_OF_SEATS"],
                "FLIGHT": ["FID", "FNO", "DEPARTURE", "ARRIVAL", "STATUS", "AIRLINEID"],
                "TICKET": ["TICKET_ID", "SEAT_NO", "CLASS", "BID", "FID", "AID", "AIRLINEID", "PID", "DEPARTING_FROM", "ARRIVING_AT"]
            }

            if choice == "Create":
                st.subheader(f"Add New Record to {table}")
                data = {field: st.text_input(f"Enter {field}") for field in fields[table]}
                if st.button("Add Record"):
                    insert_record(table, **data)
                    st.success(f"Record added to {table} successfully!")

            elif choice == "Read":
                st.subheader(f"View Records from {table}")
                records, columns = read_records(table)
                df = pd.DataFrame(records, columns=columns)
                df.index = df.index + 1
                df.index.name = 'S.No'
                st.dataframe(df)

            elif choice == "Update":
                st.subheader(f"Update Record in {table}")
                id_column = {
                    "AIRPORT": "AID",
                    "PAYMENT": "PAYID",
                    "PASSENGER": "PID",
                    "AIRLINE": "AIRLINEID",
                    "BOOKING": "BID",
                    "FLIGHT": "FID",
                    "TICKET": "TICKET_ID"
                }[table]
                id_value = st.text_input(f"Enter {id_column} to Update")
                if id_value:
                    updates = {field: st.text_input(f"New {field}") for field in fields[table] if field != id_column}
                    if st.button("Update Record"):
                        if update_record(table, id_column, id_value, **updates):
                            st.success(f"Record with {id_column} {id_value} updated successfully!")
                        else:
                            st.error(f"Record with {id_column} {id_value} not found!")

            elif choice == "Delete":
                st.subheader(f"Delete Record from {table}")
                id_column = {
                    "AIRPORT": "AID",
                    "PAYMENT": "PAYID",
                    "PASSENGER": "PID",
                    "AIRLINE": "AIRLINEID",
                    "BOOKING": "BID",
                    "FLIGHT": "FID",
                    "TICKET": "TICKET_ID"
                }[table]
                id_value = st.text_input(f"Enter {id_column} to Delete")
                if st.button("Delete Record"):
                    if delete_record(table, id_column, id_value):
                        st.success(f"Record with {id_column} {id_value} deleted successfully!")
                    else:
                        st.error(f"Record with {id_column} {id_value} not found!")
        else:
            st.warning("Please log in to access CRUD operations.")

if __name__ == "__main__":
    main()