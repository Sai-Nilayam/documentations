# %%
"""This Module focuses on how to use MySQL Database with Python.

1. Why do I need to know Database where as we already have opitions like 
storing data and query upon with CSV and Pandas, storing data in a Python 
Dictionary etc?
    Actually you can use either way. But as Databases are widely used in 
    industries so it is very possible that you might need to work with a 
    Database while doing any Mahcine Learning Task. So you need to know 
    Database.

2. Why to go for MySQL Database instead of any other?
    1. MySQL is Free so you might find it almost everywhere.
    2. MySQL is the 2nd most widely used Database after Oracle Database.

3. Do I really learn to know MySQL?
    No. MySQL is a Database software that supports SQL (Structured Query 
    Language). So all you need to learn is SQL.

4. What are different Conceptual things to learn in SQL?
    1. CRUD Operations
    2. Join Operations
    3. Creating Views
    4. SQL Index

5. What we are going to learn in this Module?
    1. Install MySQL in a Linux system.
    2. Connect to it from Python.
    3. Execute different SQL Operations
    4. How to convert the database retrived data to a Pandas Dataframe to 
    do Analysis.

6. How would you learn MySQL?
    I will just do a google search while doing anything with MySQL. As it is 
    not so difficult thing to master in advance.
"""

"""
1. How to install MySQL in Linux system?
    Following these steps are needed. 
    Linux Commands:
        1. sudo apt update
        2. sudo apt install mysql-server
        3. mysql --version
        4. sudo my_sql_secure_installation
        5. sudo mysql
            1. select user, authentication_string, plugin from mysql.user;
            2. ALTER USER 'root'@'localhost' IDENTIFIED WITH 
            mysql_native_password by 'My*21@sql';
            3. select user, authentication_string, plugin from mysql.user;
            4. exit
        6. sudo mysql -u root -p
            1. show databases;
            2. exit
        7. sudo apt install ./mysql_workbench
2. How to connect to the MySQL server from Python?
    1. pip install mysql-connector-python
    2. import the package and use it. 
"""

# Code goes here.
# For our system, the Password of MySQL is 'My*21@sql'

# For reading the database.
import mysql.connector as mysql_connector
import pandas as pd

host = 'localhost'
user = 'root'
password = 'My*21@sql'
database = 'python_database'

my_db = mysql_connector.connect(
    host=host, 
    user=user, 
    password=password,
    database=database
)

my_cursor = my_db.cursor()

sql = 'SELECT * FROM student'

my_cursor.execute(sql)
print('Query executed.')

result = my_cursor.fetchall()

my_cursor.close()
my_db.close()
print('Connection closed.')

print(result)

df = pd.DataFrame(result)
df.columns = 'Primary_Key', 'Name', 'Age'
display(df)

# Now with this data we could create dataframes using Pandas.

# %%
# For writing to the database.
import mysql.connector as mysql_connector

host = 'localhost'
user = 'root'
password = 'My*21@sql'
database = 'python_database'

my_db = mysql_connector.connect(
    host=host, 
    user=user, 
    password=password, 
    database=database
)

my_cursor = my_db.cursor()

sql = 'INSERT INTO student (name, age) VALUES ("Ana", 25)'

my_cursor.execute(sql)
my_db.commit()
print('Query executed.')

my_cursor.close()
my_db.close()
print('Connection closed.')