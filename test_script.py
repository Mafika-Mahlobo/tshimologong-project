import mysql.connector

# Set up connection parameters
MYSQL_HOST = 'localhost'
MYSQL_USER = 'Mafika'
MYSQL_PASSWORD = 'RUmah96@'
MYSQL_DB = 'SurveysDB'

try:
    # Attempt to connect to the MySQL database
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )

    # If connection is successful, print success message
    print("Database connection successful")

    # Close the connection
    conn.close()

except mysql.connector.Error as e:
    # If connection fails, print error message
    print("Error connecting to the database:", e)
