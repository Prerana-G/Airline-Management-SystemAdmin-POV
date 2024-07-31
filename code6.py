import mysql.connector
import pandas as pd
import streamlit as st
import hashlib

# Database connection
def create_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Preranag22',
        database='AirportManagement'
    )

# Hash password
def hash_password(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

# Register user
def register_user(username, pwd, role):
    hashed_password = hash_password(pwd)
    try:
        conn = create_connection()
        cursor = conn.cursor()
        query = "INSERT INTO users (username, pwd, role) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, hashed_password, role))
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

def search_records(table, search_criteria):
    conn = create_connection()
    cursor = conn.cursor()
    search_queries = []
    search_values = []

    for column, value in search_criteria.items():
        if value:
            search_queries.append(f"{column} LIKE %s")
            search_values.append(f"{value}%")

    query = f"SELECT * FROM {table} WHERE {' AND '.join(search_queries)}"
    cursor.execute(query, search_values)
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
    st.title("Airport Ticket Booking Management System")

    # Initialize session state
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
        st.session_state["username"] = None
        st.session_state["role"] = None

    # Clear the content for non-logged-in users
    if not st.session_state["logged_in"]:
        st.empty()
    
    menu = ["Register", "Login", "CRUD Operations"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Register":
        st.subheader("Create New Account")
        username = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        confirm_pwd = st.text_input("Confirm Password", type="password")
        role_code = st.text_input("Role Code")

        if st.button("Register"):
            if pwd == confirm_pwd:
                role = {
                    "EMP800": "Employee",
                    "Exec900": "Manager",
                    "BM264": "Board Member"
                }.get(role_code)
                
                if role:
                    if register_user(username, pwd, role):
                        st.success("You have successfully created an account!")
                    else:
                        st.error("Username not available. Try again with a different username.")
                else:
                    st.error("Invalid role code. Please enter a valid code.")
            else:
                st.error("Passwords do not match.")

    elif choice == "Login":
        st.subheader("Login Section")
        username = st.text_input("Username")
        pwd = st.text_input("Password", type="password")

        if st.button("Login"):
            hashed_password = hash_password(pwd)
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT role FROM users WHERE username = %s AND pwd = %s", (username, hashed_password))
            result = cursor.fetchone()
            conn.close()
            if result:
                st.success("Logged in successfully!")
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.session_state["role"] = result[0]
                
            else:
                st.error("Invalid username or password.")

    elif choice == "CRUD Operations":
        if st.session_state["logged_in"]:
            st.subheader(f"Welcome, {st.session_state['username']}!")

            # Fetch user role from the session state
            role = st.session_state.get("role", "Employee")

            st.title("Airport Ticket Booking Management")

            # Determine accessible tables based on role
            if role == "Employee":
                tables = ["PAYMENT", "PASSENGER", "BOOKING", "FLIGHT", "TICKET"]
            elif role == "Manager":
                tables = ["AIRPORT", "PAYMENT", "PASSENGER", "AIRLINE", "BOOKING", "FLIGHT", "TICKET"]
            else:  # Board Members
                tables = ["AIRPORT", "PAYMENT", "PASSENGER", "AIRLINE", "BOOKING", "FLIGHT", "TICKET"]

            menu = ["Create", "Read", "Update", "Delete"]
            choice = st.sidebar.selectbox("Select Operation", menu)

            table = st.selectbox("Select Table", tables)

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

                # Fetch records and columns
                records, columns = read_records(table)

                # Add sorting feature
                sort_by = st.selectbox("Sort by", columns, index=0)  # Default to the first column
                if sort_by:
                    # Sort records based on the selected column
                    sorted_records = sorted(records, key=lambda x: x[columns.index(sort_by)])
                    df = pd.DataFrame(sorted_records, columns=columns)
                else:
                    df = pd.DataFrame(records, columns=columns)

                # Display all records
                st.subheader("All Records")
                df.index = df.index + 1
                df.index.name = 'S.No'
                st.dataframe(df)

                # Add search feature
                st.subheader("Search Records")
                search_criteria = {field: st.text_input(f"Search by {field}", "") for field in columns}
                if st.button("Search"):
                    search_results, search_columns = search_records(table, search_criteria)
                    if search_results:
                        st.write("Search Results:")
                        df_search = pd.DataFrame(search_results, columns=search_columns)
                        df_search.index = df_search.index + 1
                        df_search.index.name = 'S.No'
                        st.dataframe(df_search)
                    else:
                        st.write("No records match your search criteria.")

            elif choice == "Update":
                st.subheader(f"Update Record in {table}")
                id_column = st.selectbox("Select ID Column", fields[table])
                id_value = st.text_input(f"Enter {id_column} of the record to update")
                if record_exists(table, id_column, id_value):
                    update_data = {field: st.text_input(f"Update {field}") for field in fields[table] if field != id_column}
                    if st.button("Update Record"):
                        update_record(table, id_column, id_value, **update_data)
                        st.success(f"Record in {table} updated successfully!")
                else:
                    st.error(f"Record with {id_column} = {id_value} does not exist.")

            elif choice == "Delete":
                st.subheader(f"Delete Record from {table}")
                id_column = st.selectbox("Select ID Column", fields[table])
                id_value = st.text_input(f"Enter {id_column} of the record to delete")
                if st.button("Delete Record"):
                    if delete_record(table, id_column, id_value):
                        st.success(f"Record with {id_column} = {id_value} deleted successfully!")
                    else:
                        st.error(f"Record with {id_column} = {id_value} does not exist.")
            
            # Logout option
            if st.button("Logout"):
                st.session_state["logged_in"] = False
                st.session_state["username"] = None
                st.session_state["role"] = None
                st.success("Click again to logout!")
                

        else:
            st.warning("Please log in to access CRUD operations.")

if __name__ == "__main__":
    main()
