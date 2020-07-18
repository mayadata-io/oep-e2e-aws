import mysql.connector
import random
from config import *
from query import *
import os
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import date, datetime, timedelta

MYSQL_HOST = ''
MYSQL_USER = ''
MYSQL_PASS = ''

try:
    MYSQL_HOST = os.environ.get('MYSQLHOST')
    MYSQL_USER = os.environ.get('MYSQLUSER')
    MYSQL_PASS = os.environ.get('MYSQLPASS')
except:
    print("error in finding the env variables ")

cnx = mysql.connector.connect(user=MYSQL_USER,
                              password=MYSQL_PASS,
                              host=MYSQL_HOST,
                              )

# _________________________________________________-< Connections Done >-_______________________________________

cursor = cnx.cursor()


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)


for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


# _________________________________________________-< Inserting Data >-_______________________________________
def insert_data(cursor, table):
    print("------------------------!! {} !!-------------------------".format(table))
    emp_no = cursor.lastrowid
    tomorrow = datetime.now().date() + timedelta(days=1)
    try:
        add_salary = genInsertQuery(table)
        for i in range(100000):
            num2 = random.randint(1000, 2000)
            valueForQuery = genQueryValue(table, tomorrow, i)
            cursor.execute(add_salary, valueForQuery)
    except mysql.connector.Error as err:
        print("Inserting Data Error :")
        print(err.msg)
# _________________________________________________-< Inserting Data :+1: >-_______________________________________


try:
    print("Inserting data into database Salaries")
    for table in TABLES:
        insert_data(cursor, table)
except mysql.connector.Error as err:
    print("Error in Inserting >>> : {}".err.msg)



cnx.commit()
cursor.close()
cnx.close()
