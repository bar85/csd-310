import mysql.connector
from mysql.connector import errorcode

# Database configuration
db_config = {
    "user": 'winery_user',
    'password': 'popcorn',
    'host': 'localhost',
    'database': 'winery'
}

# Connect to the MySQL server and create the database and tables
def execute_sql_commands(commands):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        for command in commands:
            cursor.execute(command)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# Function to display data from a table
def display_table_data(table_name):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        print(f"\nData from {table_name}:")
        for row in rows:
            print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# List of tables to display data from
tables = ['Departments', 'Employees', 'Products', 'Suppliers', 'SupplyInventory', 'Distributors', 'Distribution']

# Display data from each table
for table in tables:
    display_table_data(table)
